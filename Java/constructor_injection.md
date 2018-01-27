## Constructor Injection
- [출처](https://stackoverflow.com/a/21219567)
- 스프링에서 injection을 하는 방법으로는 setter injection과 constructor injection이 있다.
- 스프링에서는 Constructor Injection으로 코딩하는것을 권고하고 있다.

## 왜 Constructor Injection인가?
- 컨테이너에 구속받지 않고 의존성 요구를 확고히 할 수 있다.
- 생성자 인자로 의존성을 받게되는 클래스는 그 인자가 제공되어야만 인스턴스로 만들 수 있다.
- 이건 Spring을 하든 안하든 상관없이 의존성 요구를 컨테이너 독립적으로 해야한다.
- Setter Injection을 사용하게 되면 setter가 반드시 호출되도록 하기 위해서 @Required나 @Autowired를 사용해야 하는데 이 방법은 스프링에서 제공하는것으로써 컨테이너에 구속됩니다.

## 권장 방식
- spring 4.3이상부터는 `Implicit constructor injection for single-constructor(단일 생성자를 위한 묵시적 생성자 인젝션)`을 지원합니다.
- [Core container refinements in Spring Framework 4.3](https://spring.io/blog/2016/03/04/core-container-refinements-in-spring-framework-4-3)

```java
// 권장
public class FooRepository {
  private final BarRepository barRepository;
  
  public FooRepository(BarRepository barRepository) {
    this.barRepository = barRepository;
  }
}
```

```java
// 비 권장
public class FooService {
  private BarRepository barRepository;
  
  public void setBarService(BarRepository barRepository) {
    this.barRepository = barRepository;
  }
}

// 비 권장
public class FooService {
  @Autowired
  private BarRepository barRepository;
}
```
