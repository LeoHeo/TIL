[Sealed classes](https://kotlinlang.org/docs/sealed-classes.html)에 대해서는 공식 문서 설명을 참고하자

# Sealed Class 활용방법
- [Sealed Classes Instead of Exceptions in Kotlin](https://phauer.com/2019/sealed-classes-exceptions-kotlin/)

# 실전 예제
## API 호출 상황
- API를 호출하고 성공을 하면 비지니스 로직을 수행하는데 status 404, 400 response로 올때도 그에 따른 비지니스 로직이 수행되어야 함

## 공통
- RestTemplate를 통해서 API를 호출한다.
- RestTemplate을 하고 200이 아닌 이상 HttpStatusCodeException이 발생한다.

### Java
- 400, 404가 비지니스 로직상 필요하기 때문에 ErrorHandler를 재정의 해야 한다.

```java
public class JsonHolderErrorHandler implements ResponseErrorHandler {

    private static final List<HttpStatus> NOT_EXCEPTION = Arrays.asList(HttpStatus.BAD_REQUEST, HttpStatus.NOT_FOUND);

    @Override
    public boolean hasError(ClientHttpResponse response) throws IOException {
        HttpStatus statusCode = response.getStatusCode();
        return !NOT_EXCEPTION.contains(statusCode) || statusCode.is5xxServerError();
    }

    @Override
    public void handleError(ClientHttpResponse response) throws IOException {
        // 5xx Server Error 처리
        if (response.getStatusCode().is5xxServerError()) {
            throw new HttpServerErrorException(response.getStatusCode(), response.getStatusText());
        }

        if (!NOT_EXCEPTION.contains(response.getStatusCode())) {
            throw new HttpClientErrorException(response.getStatusCode(), response.getStatusText());
        }

    }
}
```

위와 같이 ErrorHandler를 만들어주고 RestTemplate을 호출할때 set을 해준다.

```java
    public ResponseEntity<PostData> getPostById(Long id) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.add("Content-Type", "application/json");

            RestTemplate restTemplate = new RestTemplateBuilder().build();
            // 새롭게 만든 에러 핸들러 적용
            restTemplate.setErrorHandler(new JsonHolderErrorHandler());
            return restTemplate.exchange("https://jsonplaceholder.typicode.com/asd/{id}", HttpMethod.GET, new HttpEntity<>(null, headers), PostData.class, id);
        } catch (HttpStatusCodeException e) {
            /**
             * 인제 400, 404가 아닐때만 Catch에 잡힌다.
             */
            throw new ApiException(e.getStatusCode().value(), e.getResponseBodyAsString());
        }
    }
```

그러면 인제 이걸 호출하는 메소드쪽에서는 아래와 같은 메소드가 나온다.

```java
    public void getPostById(Long id) {
        ResponseEntity<PostData> responsePost = jsonHolderService.getPostById(id);
        HttpStatus statusCode = responsePost.getStatusCode();

        if (statusCode == HttpStatus.BAD_REQUEST) {
            // BAD_REQUEST do something
            return;
        }

        if (statusCode == HttpStatus.NOT_FOUND) {
            // NOT_FOUND do something
            return;
        }

        PostData body = responsePost.getBody();
        System.out.println(body);

        // success do something
    }
```

Java에서는 Custom ErrorHandler도 만들어줘야 하는 귀찮은 상황이 발생한다.

### Kotlin Selead Class 활용

위와 똑같은 요구사항을 kotlin에서 Selead class를 활용해서 처리해보자

```kotlin
sealed class JsonHolderResult {
    data class Success(val postDto: PostDto): JsonHolderResult()
    data class Error(val status: HttpStatus, val exception: Exception? = null): JsonHolderResult()
}

@Service
class JsonHolderService {
    fun getPostById(id: Long): JsonHolderResult = try {
        val headers = HttpHeaders()
        headers.add("Content-Type", "application/json")

        val restTemplate = RestTemplateBuilder().build()
        val body = restTemplate.exchange(
            "https://jsonplaceholder.typicode.com/posts/{id}",
            HttpMethod.GET,
            HttpEntity(null, headers),
            PostDto::class.java,
            id
        ).body

        JsonHolderResult.Success(body!!)
    } catch (e: HttpStatusCodeException) {
        JsonHolderResult.Error(status = e.statusCode, exception = e)
    }
}
```

Selead Class를 통해서 API에 대한 Success, Error를 하는 JsonHolderResult를 만들어보자

인제 호출 하는 부분 코드를 보자

```kotlin
    fun getPostById(id: Long) {
        when (val postResponse = jsonHolderService.getPostById(id)) {
            is JsonHolderResult.Success -> {
                // sucess do something
                println("Success DTO: ${postResponse.postDto}")
            }
            is JsonHolderResult.Error -> {
                when (postResponse.status) {
                    // error do something
                    HttpStatus.NOT_FOUND -> println("Not Found")
                    HttpStatus.BAD_REQUEST -> println("BAD Request")
                    else -> throw ApiException(postResponse.status.value(), postResponse.exception?.message)
                }
            }
        }
    }
```

인제 Java 코드와 비교해보자

1. ErrorHandler를 굳이 안만들어도 된다.
2. 메소드 시작 부분에 if 문으로 에러 체크 하는 부분이 사라졌다.

Sealed Class를 통해서 Success, Error 부분이 명확히 나눠지니 개인적으로 코드가 훨씬 보기 좋다

위에 블로그 예시를 통해서 1차적으로 RestTemplate를 선언하고 2차적으로 ResTemplate을 또 선언할때 아래와 같은 코드가 될 수 있다.

```java
try {
    val profile = client.requestUserProfile(userId)
    try {
        val image = client.downloadImage(profile.avatarUrl)
        processImage(image)
    } catch (ex: ImageDownloadException) {
        queueForRetry(userId, ex.message)
    }
} catch (ex: UserProfileClientException) {
    showMessageToUser(userId, ex.message)
} catch (ex: SuspiciousException) {
    // which method throws this exception?
    // requestUserProfile()? downloadImage()? processImage()? queueForRetry()?
}
// have we forgot to catch an exception? Who knows.
```

> Again, what’s wrong here?
>
> 1. The code is hard to read due to the try-catch-ceremony.
> 2. It’s not obvious anymore which exception comes from which method. Yes, good naming can help here.
> 3. It’s hard to say if we have caught all possible exceptions. It’s easy to introduce a bug here.
> 4. It becomes hard to follow the execution flow because it can stop at some point and continues at another point (and depth in the call stack!). Code with multiple exceptions which are thrown and caught at multiple points can lead to code which is hard to understand. I often had to jump forward and back in our code base to understand the path that an exception has made.


위 코드를 Selead class를 이용하면 어떻게 바뀔 수 있을까?

```kotlin
when (val profileResult = client.requestUserProfile(userId)) {
    is UserProfileResult.Success -> {
        when (val imageResult = client.downloadImage(profileResult.userProfile.avatarUrl)){
            is ImageDownloadResult.Success -> processImage(imageResult.image)
            is ImageDownloadResult.Error -> queueForRetry(userId, imageResult.message)
        }
    }
    is UserProfileResult.Error -> showMessageToUser(userId, profileResult.message)
}
```

Selead Class를 활용하면 이렇개 깔끔하게 코드를 짤 수 있다.