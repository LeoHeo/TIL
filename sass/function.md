## Sass variable Function

sass variable에서 `fade-in`, `fade-out`를 사용할 경우 아래와 같이 쓸 수 있다.

```css
$lagoon-blue: fadeout(#62fdca, 0.5);

.math {
  background-color: $lagoon-blue; //괄호 없이 변수명만
}
```

## Sass allow mathematical

css color을 지정할 경우 명시적으로 지정을 해줘야 한다.

근데 sass에서는 수학적인 계산이 가능하다.

1. addition(더하기) `+`
2. subtraction(빼기) `-`
3. multiplication(곱하기) `*`
4. division(나눗셈) `/`
5. modulo(나머지 연산은 `정수` ) `%`


예를들어 `color: magenta;`를 지정한다고 했을때

```css
.math {
  color: magenta;
}
```

위와 같이 쓰는데 sass에서는 아래같이 쓸 수 도 있다.

`red`, `green`, `blue`를 조합할 수 있다.

```css
.math {
  color: red + blue;
}
```

또한 숫자끼리 연산도 가능하다.

```css
.math {
  color: #010203 + #040506;
}
```

```css
// width에 따른 height, line-height, border-radius설정

$width: 250px;

.math {
  width: $width;
  height: $width/6;
  line-height: $width/6;
  border-radius: $width/30;
}
```
