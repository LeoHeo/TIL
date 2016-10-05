## What is a potential pitfall with using typeof bar === "object" to determine if bar is an object? How can this pitfall be avoided?

많은 사람들이 빠지는 함정중에 하나가 아래와 같은 코드이다.

많은 개발자들이 `console.log(typeof bar === "object")`를 `true`로 기대하지만 결과값은 `false`이다.

예상한대로 `true`가 나올라면 `var foo = null`이라고 변수선언을 하고 그 다음에 log를 찍어보면 true가 된다.

```javascript
console.log(typeof bar === "object") // false

var foo === null
console.log(typeof bar === "object") // true
```

그래서 해결방법으로는 아래와 같다.

```javascript
console.log((bar !== null) && ((typeof bar === "object") || (typeof bar === "function")));

// 배열도 체크할라면 Jquery 사용시
console.log((bar !== null) && (typeof bar === "object") && (! $.isArray(bar)));
```


## What will the code below output to the console and why?

```javascript
var myObject = {
    foo: "bar",
    func: function() {
        var self = this;
        console.log("outer func:  this.foo = " + this.foo);
        console.log("outer func:  self.foo = " + self.foo);
        (function() {
            console.log("inner func:  this.foo = " + this.foo);
            console.log("inner func:  self.foo = " + self.foo);
        }());
    }
};
myObject.func();

// outer func:  this.foo = bar
// outer func:  self.foo = bar
// inner func:  this.foo = undefined
// inner func:  self.foo = bar
```

맨처음 `self` 와 `this`는 같은 `myObject`를 가르킨다. 그러기 때문에 둘다 `bar`가 나오는데

아래 closure문법에서의 `this`는 `global window`객체를 가르키기 때문에 `undefined`가 뜨고, `self`가 가르치고 있는 `this`는 아직 `myObject`이기 때문에 `bar`가 출력된다.


## function Declaration and Expression
자바스크립트에서 함수의 선언과 표현에는 차이점이 있다.

### Declaration
- 미리 자바 스크립트의 실행 컨텍스트(execution context)에 로딩 되어 있으므로 언제든지 호출할 수 있지만

### Expression
- 인터프리터가 해당 라인에 도달 하였을때만 실행

```javascript
// 1번
console.log(foo()); // test logged
function foo() {
	return "test";
}

// 2번
console.log(bar()); // bar is not function
var bar = function() {
	return "test";
};
```

### 1, 2번 실행될때
```javascript
// Declaration 선언된걸 모두 위로 올림
// 그래서 아래와 같이 실행됨
function foo() {
	return "test";
}
console.log(foo());

// 하지만 2번은 Declaration가 아니기 때문에 위로 올리지 않음
// 그래서 아래와 같은 실행됨
var bar = undefined;
console.log(bar());
bar = function() {
	return "test";
}
```
