# JPA 엔티티 매핑

## @Entity
- 기본생성자는 필수다 -> 파라미터가 없는 public 또는 protected 생성자
- final 클래스, enum, interface, inner 클래스에는 사용할 수 없다.
- 저장할 필드에 final을 사용하면 안 된다.

## @Table
- 엔티티와 매핑할 테이블 이름
- 생략하면 엔티티 이름을 테이블 이름으로 사용
- UniqueConstraint -> 제약조건 추가
- 이런 DDL 구문들은 자동 생성할때만 사용되고 JPA의 실행로직에는 영향을 주지 않는다.

```
- catalog -> catalog 기능이 있는 데이터베이스에서 catalog를 매핑
- schema -> schema 기능이 있는 데이터베이스에서 schema를 매핑
- uniqueConstranints -> 스키마 자동 생성 기능을 사용해서 DDL를 만들때만 사용
```

## @Column
- 주로쓰는거 3개
- name, nullable, length
- @Column(name = "NAME", nullable = false, length = 10) 

## @Id, @GeneratedValue
- @Id 애노테이션만 있는경우는 애플리케이션에서 Id를 직접할당
- 자동생성되는 `AUTO_INCREMENT`같은 경우에는 `@GeneratedValue`도 추가해줘야 한다.
- IDENTIITY 식별자 생성 전략은 엔티티를 데이터베이스에 저장해야 식별자를 구할 수 있으므로 em.persist()를 호출하는 즉시 INSERT SQL이 `데이터베이스에 전달` -> 트랜잭션을 지원하는 쓰기 지연이 동작하지 않는다.

## @SequenceGenerator
- 시퀸스 식별자 생성기
- `allocationSize: 50` -> 시퀸스 한 번 호출에 증가하는 수 -> 기본값 50
