## Evaluation Strategies and Termination

### Call-by-value & Call-by-name
- 종료라는 관점에서 `CBN`과 `CBV`를 비교해보자

`CBV`가 종료될 수 있다면, `CBN`도 항상 종료가 될 수 있다.  
하지만 `CBN`이 종료가 된다고 해서 `CBV`가 항상 종료가 되지는 않는다.

왜 항상 종료가 되지 않는지? 그런상황이 어떤상황인지 한번 예를 들어 살펴보자.

```scala
def first(x: Int, y: Int) = x

// Under CBN
// CBN은 인자를 줄이지 않고
// first 함수를 실행하기 때문에
// 바로 1를 반환한다.
first(1, loop)


// Under CBV
// CBV는 인자를 줄여야 하기 때문에
// loop를 줄일려고 계속 반복적인 실행을
// 할 것이고 무한루프에 빠진다.
first(1, loop)
```

### Scala normally uses call-by-value
- 스칼라는 기본적으로 `call-by-value`를 씁니다.

그러면 `CBN`이 `CBV`가 더 잘 종료가 될 수 있다는 장점이 있는데도 왜 `CBV`를 쓰느냐? 라는 의문이 생길 수 있습니다. `실제 표현식들에서 CBV는 인수들을 반복해서 계산하지 않기때문에 CBN보다 효율적이다. 또한 CBV는 명령형 프로그래밍과 side-effect 관련해서 더 좋다. 스칼라 또한 명령형 언어의 측면이 있기 때문에 CBV를 기본적으로 채택한다.`

## Scala uses call-by-name
- 스칼라에서 그럼 `call-by-name`을 사용할때는 어떻게 해야 하는가?
- 화살표 파라미터 타입 앞에 더하면 된다.

```scala
// =>로 CBN 만들수있다.
def constOne(x: Int, y: => Int) = 1

// 두 개의 차이점
constOne(1+2, loop)
constOne(loop, 1+2)
```

```scala
// 첫번째는 CBV
// 두번째는 CBN
// 그렇기 때문에 1+2는 3이 된다.
// 그리고 loop는 그대로 계산을 안하고 전달
constOne(1+2, loop) // result = 1

// 첫번째는 CBV
// 두번째는 CBN
// 그렇기 때문에 loop를 계산하기 위해서 무한루프
constOne(loop, 1+2)
```
