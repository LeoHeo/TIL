## 데이터와 변수 타입

### 리터럴(literal)
- 숫자 5, 문자 A, 텍스트 'Hello, world'처럼 소스 코드에 등장하는 데이터

### String interpolation
- 값 또는 변수를 String 내에 결합시키는 보다 직접적인 방식은 외부 값과 변수명을 인식하고 해석하는 특수모드인 문자열 보간(string interpolation)을 사용하는 것이다. 스칼라에서 문자열 보간은 문자열의 첫 큰 따옴표 전에 접두사 `s`를 추가하여 표기한다. 그런 다음, 달러 기호(`$`)(선택적으로 중괄호를 함께 쓰기도 한다)

```scala
val item = apples

// 문자열 보간
s"How do you like them ${item}?"
-> How do you like them apples?

s"Fish n chips n vineger, ${"pepper" * 3} salt"
-> Fish n chips n vineger, pepper pepper pepper salt

// printf 보간 기법
f"I wrote a new $item.%3s today"
-> I wrote a new app today

f"Enjoying this $item ${355 / 113}.%5f times today"
-> Enjoyinh this apples 3.14159 times today
```
