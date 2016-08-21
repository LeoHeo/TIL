## Sass

## Sass

[Sass](http://sass-lang.com/)란?
Syntactically Awesome Style Sheets의 약어
Awesome하게 CSS를 만들수 있다.

## Sass Install & Compile
[참고 링크](https://github.com/yamoo9/FDS/blob/65aac73b0674054bbf0edc075ca7b72cc6712b85/Lecture/DAY22/README.md)

Browser가 `scss`파일을 인식하지 못하기 때문에 `css`로 compile해줘야 한다.

### 플랫폼
- Node.js -> [Node Sass](https://github.com/sass/node-sass/)
- Ruby -> Ruby Sass(컴파일 속도가 느림)

### 설치

```
$ npm install node-sass --global
```

### Compile

```
# node-sass [Sass 파일 이름] [컴파일 될 CSS 파일 이름]
$ node-sass sass/style.scss css/style.css
```

### Folder Complie
```
$ node-sass sass/ --output css/
```

### File Watch Compile
```
# node-sass -watch sass/ --output css/
$ node-sass -w sass/ -o css/
```

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
$standard-border: 4px solid black;

.banner {
  border: {
    top: $standard-border;
    bottom: $standard-border;
  }
}
```

위와 같이 쓸 수 있다.

Sass는 arrays Not Suppored

## pseudo-element

아래와 같은 CSS pseudo-element가 있다.

```css
.notecard:hover {
  transform: rotatey(-180deg);
}
```

Sass에서는 pseudo-element에 대해서 아래와 같이 선언할 수 있다.

```css
.notecard{ 
  &:hover{
      @include transform (rotatey(-180deg));  
    }
}
```

## mixin & include

위의 코드에서 `@include`가 나왔었다.

`@include` & `@mixin`을 사용하면 반복적인 작업을 한층 더 줄일 수 있다.

위에서 `$name`로 변수를 선언해서 불러올 수 있었다.

근데 만약에 Crossbrowsing문제로 인해 여러줄을 변수로 지정할라면?!

아래와 같은 CSS 코드가 있고 `backface-visibilty`라는 속성을 다른곳에서 또 써야 한다면?!

```css
.notecard .front, .notecard .back {
  width: 100%;
  height: 100%;
  position: absolute;

   backface-visibility: hidden;
  -webkit-backface-visibility: hidden; 
  -moz-backface-visibility: hidden;
  -ms-backface-visibility: hidden;
  -o-backface-visibility: hidden;
}
```

```css
@mixin backface-visibility {
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -ms-backface-visibility: hidden;
  -o-backface-visibility: hidden;
}

.notecard {
.front, .back {
    width: 100%;
    height: 100%;
    position: absolute;

    @include backface_visibility;
  }
}
```

`mixin` & `include`를 사용하면 위와 같이 사용할 수 있다.

근데 만약 위 코드에서 `hidden`이 아니라 다른속성을 지정할라면?! 어떻게 해야할까?!

`mixin`을 속성별로 만드는건 너무 비효율적이다.

그래서 `Sass`에서도 `mixin`을 함수처럼 사용할 수 있다.

`Arguments`를 받아서 그 변수로 속성값을 지정할 수 있다.

그래서 위의 코드를 아래와 같이 바꿀 수 있다.

```css

@mixin backface-visibility($visibility) {
  backface-visibility: $visibility;
  -webkit-backface-visibility: $visibility;
  -moz-backface-visibility: $visibility;
  -ms-backface-visibility: $visibility;
  -o-backface-visibility: $visibility;
}

.notecard {
.front, .back {
    width: 100%;
    height: 100%;
    position: absolute;

    @include backface_visibility(hidden);
  }
}
```

또한 `Default`값을 명세 할 수도 있다.

아래와 같이 `Argument: property`로 지정할 수 있다.

```css

@mixin backface-visibility($visibility: hidden) {
  backface-visibility: $visibility;
  -webkit-backface-visibility: $visibility;
  -moz-backface-visibility: $visibility;
  -ms-backface-visibility: $visibility;
  -o-backface-visibility: $visibility;
}

.notecard {
.front, .back {
    width: 100%;
    height: 100%;
    position: absolute;

    @include backface_visibility();
  }
}
```

위와 같이 mixin으로 확장성을 높일 수 있다. Sass 만세~

### mixin 5 important facts
1. mixin은 여러개의 Arguments를 가질 수 있다.
2. mixin은 `@include`를 사용해서 불러올수 있다.
3. named parameter(Arguments:value)를 사용할수도 있다.
4. default값을 명세해야 할 경우 맨 마지막에 명세를 해야한다.
5. mixin안에서도 중첩 sass가 가능하다.

```css
// default값은 맨 뒤로
@mixin dashed-border($width, $color: #FFF) {
  border: {
     color: $color;
     width: $width;
     style: dashed;
  }
}

span { //default값을 명세 안하는 경우
    @include dashed-border(3px);
}

p { //named parameter를 사용안하는 경우
    @include dashed-border(3px, green);
}

div { //named parameter를 사용하는 경우
   @include dashed-border(color: purple, width: 5px); 
}
```

### mixin multiple arguments allow list or map

Sass Mixin으로 값을 넘길때 list나 map으로도 전달 할 수 있다.

여기서 전달할때 정말 `별표 100개`해야 하는것이 `$name...`이라는 것이다.

`변수이름만 쓰면 안된다.` 꼭 변수이름뒤에 `...`를 `명세`해줘야 한다!!

``` css
@mixin stripes($direction, $width-percent, $stripe-color, $stripe-background: #FFF) {
  background: repeating-linear-gradient(
    $direction,
    $stripe-background,
    $stripe-background ($width-percent - 1),
    $stripe-color 1%,
    $stripe-background $width-percent
  );
}

// map형식
$college-ruled-style: ( 
  direction: to bottom,
  width-percent: 15%,
  stripe-color: blue,
  stripe-background: white
);

// list 형식
$stripe-properties: to bottom, 15%, blue, white;

.definition {
  width: 100%;
  height: 100%;
  @include stripes($college-ruled-style...);
  // @includce stripes($stripe-properties...);
}
```

## Sass String interpolation

mixin에서 변수로 받은 값을 String으로 쓰고자 할때

`#{$variable}`로 사용하면 된다.

```css
@mixin photo-content($file) {
  content: url(#{$file}.jpg); //string interpolation
  object-fit: cover;
}

.photo { 
  @include photo-content('titanosaur');
  width: 60%;
  margin: 0px auto; 
}
```
