# @Column 생략

## int primitive
- int 자바 기본 타입에는 null값을 삽입할 수 없으므로 not null
```
int data1; // @Column 생략, primitive 타입
data1 integer not null // 생성된 DDL -> not null이 default
```

## Integer wrapper
- Integer wrapper에는 null값을 삽입할 수 있으므로 null
```
Integer data2; // @Column 생략, 객체 타입
data2 integer // 생성된 DDL -> null이 default
```

## @Column
- @Column은 기본값이 `nullable=true`이다.

```
@Column
int data3;  // @Column 사용, 자바 기본 타입
data3 integer // 생성된 DDL
```
