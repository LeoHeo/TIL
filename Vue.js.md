## Vue.js

### props 사용할때
- template props사용할때는 `camelCase`
- HTML에서 props사용할때는 `kebab-case(하이픈 구분)`

```javascript
Vue.component('child', {
	props: ['myMessage'],
	template: '<span>{{ myMessage }}</span>'
})
```

```html
<child my-message="안녕하세요!"></child>
```

### 컴포넌트를 만들때 data는 반드시 함수여야 합니다.
- `Vue.component`로 하지 않는 경우에는 아래와 같습니다.
- [data-는-반드시-함수여야합니다 공식문서](http://kr.vuejs.org/v2/guide/components.html#data-는-반드시-함수여야합니다)

```javascript
new Vue({
	el: "#app",
  data: {
  	status: 'Critical'
  },
  template: '<p>Server Status: {{ status }} </p>'
});
```

**하지만 컴포넌트를 사용할때 위와같은 코드는 아래와 에러를 나타냅니다.**

`warning`이 발생하는 이유는 `data는 컴포넌트 인스턴스의 함수`여야합니다

```javascript
/*
Vue.component('my-cmp', {
  data: {
  	stauts: 'Critical'
  },
  template: '<p>Server Status: {{ status }} </p>'  
});
*/

// vue.js:525 [Vue warn]: The "data" option should be a function that returns a per-instance value in component definitions. 
// [Vue warn]: Property or method "status" is not defined on the instance but referenced during render. Make sure to declare reactive data properties in the data option. 
```

그래서 아래와 같이 해야합니다.

```javascript
Vue.component('my-cmp', {
	data: function() {
  	return {
    	status: 'Critical'
    }
  },
  template: '<p>Server Status: {{ status }} </p>'  
});
```



### V-bind, v-model

``` html
<!-- v-bind는 속성을 주고자 할때 -->

<!-- Normal -->
<span title="title"/>

<!-- Vue.js -->
<span v-bind:title="title"/>
<span :title="title"/>


<!-- v-model은 data property를 주고자 할때 -->

<!-- Normal -->
<span title="title"> Hello world </span>

<!-- Vue.js -->
<!-- hello라는 property에 hello world에 저장 -->
<span v-bind:title="title"> {{hello}} </span>
<span :title="title"> {{hello}} </span>
```



