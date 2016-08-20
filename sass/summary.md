## Sass

## Sass Compile
Browser가 `scss`파일을 인식하지 못하기 때문에 `css`로 compile해줘야 한다.
`sass main.scss main.css`

## Class Nested Selector

CSS를 작성하다보면 아래와 같은 경우가 많이 발생한다.
부모안에 자식
그 자식의 span태그

```css
.banner {
  background-image: url("lemonade.jpg");
  border-top: 4px solid black;
  border-bottom: 4px solid black;
}

.banner .slogan {
  text-align: center;
}

.banner .slogan span {
  font-size: 24px;
}
```

위에서 문제점은 `.banner`은 3번이나 반복되었으며, `.slogan`은 2번이나 반복되었다.

`sass`를 사용하면 아래와 같이 만들 수 있다.

```css
.banner { 
  background-image: url("lemonade.jpg");
  border-top: 4px solid black;
  border-bottom: 4px solid black;

  .slogan { 
    text-align: center;

    span { 
      font-size: 24px;
    }
  }
}
```

위와 같이 계층적으로 CSS를 짤수 있다.

아까 `반복`되던 class명을 적지 않을 수 있어서 효과적이다.

## nest common CSS properties

sass는 commin CSS properties도 `:`로 묶을수 있다.

위의 CSS코드에서 `border`를 아래와 같이 묶을 수 있다.

```css
.banner {
  border: {
    top: 4px solid black;
    bottom: 4px solid black;
  }
}
```


## Variables in SCSS

Sass에서는 변수를 선언해서 그 변수를 불러 올 수 있다.

이게 왜 유용하냐면 기존 CSS는 이런 변수선언이 없어서 공통되는 속성을 4번썼다고 하면 `4번 쓰인 곳` 모두를 수정해줘야 했다.

변수의 유용함은 코딩을 해본사람이면 누구나 알거라고 생각한다.

Sass에서 변수선언 방법은 `$name` 이다.

위의 CSS에서 `.slogan`에 `backgroud-color`를 변수로 선언해보자

```css
$translucent-white: rgba(255, 255, 255, 0.3);

.slogan {
  background-color: $translucent-white;
}
```

위와 같이 쓸 수 있다.


