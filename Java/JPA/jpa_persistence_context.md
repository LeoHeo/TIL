## Persistence Context
- @Entity 붙인 클래스 엔티티를 영속 컨텍스트(Persistence Context)로 관리한다.
- Persistence Context는 JPA가 관리하는 Entity 객체 집합
- Persistence Context에 보관된 객체를 영속 객체(Persistent Object)라고 한다.
- Persistence Context는 세션(Entity Manager)단위로 생긴다.
- 세션 생성 시점에 영속 컨텍스트가 생성되고 세션 종료 시점에 컨텍스트가 사라진다.

## LifeCycle
1. EntityManager create
2. Transaction begin
3. EntityManager를 통해 영속 컨텍스트에 객체를 추가하거나 구한다.
4. Transaction commit -> 에러가 날 경우 rollback
5. EntityManager close
