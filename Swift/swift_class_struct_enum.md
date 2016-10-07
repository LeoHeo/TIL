## Class && Struct, enum
### Class
- 상속 가능
- Reference Type(Heap Memory) -> 동적으로 할당되는 메모리 영역
- 포인터(메모리 주소)로 전달


### Struct, enum
- 상속 불가능
- Value Type

## Value && Reference

### Value(Struct and enum)
```swift
// y가 값 타입이라면
// x에 y값을 복사
// x값을 바꿔도 y는 아무영향이 없음
var x = y
```

- 함수의 모든 인자는 상수, 물론 그 안으로 복사하는것 가능
- 구조체나 enum이 바뀔지도 모른다고 표시를 하게 만드는 `mutating` -> mutating func
- 다른 포인터을 갖고 있다가 값이 바뀌려고 하자마자 그때 복사가 됨 성능향상을 위한 절차

### Reference(class)
```swift
// y가 클래스이면 y에게 메세지를 보내면 x에게도 보내진다.
```

- 힙 메모리에 저장되어 있다가 참조를 준다.
- 참조는 자동으로 카운트가 된다. 즉, GC(Garbage Collection)가 없다.
- 그래서 나온게 `weak`, `strong`
