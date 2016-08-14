## 처음 서버를 샀습니다. 어떤 보안적 조치를 먼저 하시겠습니까?

- SSH 포트(22) 빼고는 다 막는다.

## 왜 Apache보다 Nginx가 성능이 좋을까요? node.js가 성능이 좋은 이유와 곁들여 설명할 수 있을까요?

- node.js & Nginx는 이벤트기반
- Apache같은 웹서버들은 모든 요청마다 시스템 쓰레드를 생성하는 쓰레드 기반 (Thread/Process)


## node.js는 일반적으로 빠르지만 어떤 경우에는 쓰면 안될까요?
- node 는 자신의 프로세스 내/외부에서 발생하는 모든 request를 main thread를 통해 처리한다. 이 때문에 main thread 를 잠깐 멈추게 하는 cpu-intensive javascript 코드를 수행해야 하는 usecase는 node에서 사용하기엔 무리가 있다.
- CPU Intensive한것들이라면 예를들어, 데이터분석, 딥러닝, 머신러닝할때 사용하는 수학연산들

## CDN이란? 장단점
- 인터넷상에서 가장 가까운 곳의 서버로 컨텐츠를 전송받아 트래픽이 특정 서버에 집중되지 않고 각 서버로 분산되도록 하는기술입니다.

### 장점
- 제이쿼리는 웹상에서 어디에서든 흔히 볼 수 있습니다. 여러분의 페이지에 방문한 사람들은 이미 구글 CDN을 사용하는 사이트를 방문했었을 확률이 매우 높습니다. 그러므로 제이쿼리 파일은 이미 방문자의 브라우저에 캐쉬되어있을 것이므로 여러분의 페이지에서 다시 다운로드 받을 필요가 없습니다.

### 단점
- 로드하려는 파일이 있는 서버가(보통 구글)이 다운이 된다면 파일을 가져올 수가 없어서 자신의 페이지 또한 레이아웃이 엉망이 되거나, 자바스크립트로 작성한 구문이 작동되지 않을 수 있다는 단점이 있다.


## 인덱스 장, 단점
- 어떤건 인덱스로 잡을 것인가?
- 성별(1/2), 성(1/1000), 이름(1/10000)
- 이 경우에는 이름을 인덱스로 잡는게 좋음

### 장점
- 검색 속도가 무척 빨라질 수 있다. (반드시 그런것은 아니지만)

### 단점
- 인덱스가 데이터베이스 공간을 차지해 추가적인 공간이 필요해진다
- INSERT,UPDATE속도 저하
해당 TABLE에 INDEX을 주게되면 INSERT,UPDATE가 조금 느려집니다.
왜냐하면 매번 해당 table과 table의 index를 검사해야 하기때문에 해당 table만 검사했을때보다
느리다. 

## ACID
- 원자성(Atomicity)은 트랜잭션과 관련된 작업들이 부분적으로 실행되다가 중단되지 않는 것을 보장하는 능력이다. 예를 들어, 자금 이체는 성공할 수도 실패할 수도 있지만 보내는 쪽에서 돈을 빼 오는 작업만 성공하고 받는 쪽에 돈을 넣는 작업을 실패해서는 안된다. 원자성은 이와 같이 중간 단계까지 실행되고 실패하는 일이 없도록 하는 것이다.

- 일관성(Consistency)은 트랜잭션이 실행을 성공적으로 완료하면 언제나 일관성 있는 데이터베이스 상태로 유지하는 것을 의미한다. 무결성 제약이 모든 계좌는 잔고가 있어야 한다면 이를 위반하는 트랜잭션은 중단된다.

- 고립성(Isolation)은 트랜잭션을 수행 시 다른 트랜잭션의 연산 작업이 끼어들지 못하도록 보장하는 것을 의미한다. 이것은 트랜잭션 밖에 있는 어떤 연산도 중간 단계의 데이터를 볼 수 없음을 의미한다. 은행 관리자는 이체 작업을 하는 도중에 쿼리를 실행하더라도 특정 계좌간 이체하는 양 쪽을 볼 수 없다. 공식적으로 고립성은 트랜잭션 실행내역은 연속적이어야 함을 의미한다. 성능관련 이유로 인해 이 특성은 가장 유연성 있는 제약 조건이다. 자세한 내용은 관련 문서를 참조해야 한다.

- 지속성(Durability)은 성공적으로 수행된 트랜잭션은 영원히 반영되어야 함을 의미한다. 시스템 문제, DB 일관성 체크 등을 하더라도 유지되어야 함을 의미한다. 전형적으로 모든 트랜잭션은 로그로 남고 시스템 장애 발생 전 상태로 되돌릴 수 있다. 트랜잭션은 로그에 모든 것이 저장된 후에만 commit 상태로 간주될 수 있다.
