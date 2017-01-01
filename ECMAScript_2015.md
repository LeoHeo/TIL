# ECMAScript 2015

[Egg Head learn ES6 ](https://egghead.io/courses/learn-es6-ecmascript-2015)

위의 무료강의를 보고 정리를 해봄. 계속 업데이트 할 예정

## Arrow Function

#### ECMAScript 2015 이전

```javascript
var deliveryBoy = {
  name: 'John',
  handleMessage: function(message, handler) {
  	handler(message);
  },
  receive: function() {
	var that = this;
    
    this.handleMessage("Hello, ", function(message) {
    	that.name; // get the proper name
      console.log(message + that.name);
    });
  }
};

deliveryBoy.receive();
```



#### ECMAScript 2015

```javascript
var deliveryBoy = {
  name: 'John',
  handleMessage: function(message, handler) {
  	handler(message);
  },
  receive: function() {
    /*
    this.handleMessage('Hello, ', (message) => {
    	console.log(message + this.name);
    });
    */
    
    // 축약형
    this.handleMessage('Hello, ', (message) => console.log(message + this.name));
  }
};

deliveryBoy.receive();
```



## let Keyword in ECMAScript 2015

- javascript에서 변수선언하는 `var`는 다른언어와 다른 특성이 있다.
- 그래서 간혹 아래와 같은 불편한 상황이 생긴다.

```javascript
var fs = [];

for(var i=0; i<10; i++) { 
  fs.push(function() {
  	console.log(i);
  });
}

fs.forEach(function(f) {
	f(); // 10이 열번 찍힘
});
```



**그래서 `Closure`를 쓴다며 `push`부분을 아래처럼 작성하기도 했다.**

```javascript
  fs.push((function() {
  	console.log(i);
  })());
```



#### 하지만 `let`을 사용하면 훨씬 간편해진다. 

- `let`은 쉽게 말해 `지역변수`같은 개념이다.

```javascript
for(let i=0; i<10; i++) {
	fs.push(() => console.log(i));
}
```

 

그래서 전체코드는 아래와 같다.

```javascript
var fs = [];

for(let i=0; i<10; i++) {
	fs.push(() => console.log(i));
}

fs.forEach(function(f) {
	f();
});
```



#### var일때와 let일때의 차이점

```javascript
/*
	모든함수가 Hoisting되어서 아래와 같이 된다.
*/
function varFunc() {
  var previous = 0;
  var current = 1;
  var i;
  var temp;
  var n = 10;
  
  for(i=0; i<n; i++) {
  	temp = previous;
    previous = current;
    current = temp + current;
  }
}
```

```javascript
/*
	Hoisting이 되지 않아 아래와 같이 된다.
*/
function letFunc() {
	var previous = 0;
  var current = 1;
  var n = 10;
  
  for(let i=0; i<n; i++) {
  	let temp = previous;
    previous = current;
    current = temp + current;
  }
}
```



## Shorthand Properties in ES2015

나는 `property`를 만들때 습관적으로 아래와 같이 쓴다.

```javascript
var firstName = "John";
var lastName = "Lind";

var fullName = {
  "firstName": firstName, 
  "lastName": lastName
};

console.log(fullName);

// 근데 앞으로는 아래와 같이 써도 log값이 똑같다.
let firstName = "John";
let lastName = "Lind";

let fullName = {firstName, lastName};

console.log(fullName);

// 위와 같이 쓰면 아래와 같은것도 가능하다.
let mascot = "Moose";

let team = {fullName, mascot}

/*
	fullName: {
      firstName: "John",
      lastName: "Lind"
	},
	mascot: "Moose"
*/
console.log(team);
```



## ES2015 spread operator

- `spread operator` => `전개 연산자` 라고 번역해서 부르지만 뭔가 어색하다.
- python에서의  `unpack` 개념인거 같다.
- [MDN Ref](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Spread_operator)

```javascript
console.log([1, 2, 3]); // [1, 2, 3]
console.log(...[1, 2, 3]); // 1, 2, 3

/*
	기존 Array에 다른 Array를 push할때
*/
let first = [1, 2, 3];
let second = [4, 5, 6];

// [1, 2, 3, [4, 5, 6]]
// first.push(second);
// console.log(first);

// [1, 2, 3, 4, 5, 6]
first.push(...second);
console.log(first);

/*
	first의 값을 모두 더하고자 할때 아래와 같이 쓸 수도 있음
*/
function addThreeThings(a, b, c) {
  result = a + b + c;
  return result;
}

console.log(addThreeThings(...first));
```

