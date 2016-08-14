# React
- 프레임워크가 아닌 라이브러리
- UserInterFace를 만들기 위한 라이브러리
- 가볍다

## AngularJS를 대체할 수 있을까?
- 서로의 비교대상이 아니라고 봄
- React는 프레임워크가 아니기 때문에 비교대상이 아님
- 향후 Angular2 native에서 React native 사용할 예정
- 필요할때 적절하게 골라서 사용

## VirtualDOM

실제 DOM을 업데이트하면 느려질수 있다.
`Virtual DOM`은 이걸 추상화 시킨것

```javascript
{
    name: 'test',
    point: 100
}
```

위 값이 업데이트할때마다 DOM을 바꾸어야함

[Virtual DOM에대한 설명](https://www.youtube.com/watch?v=BYbgopx44vo)

## 장, 단점
### 장점
- Virtual DOM 사용
- 배우기에 간단하다. 복잡함이 별로 없다.
- Component단위
- 뛰어난 GC
- 메모리 관리
- 다른 프레임워크나 라이브러리 혼용가능

### 단점
- 잘못사용하면 비효율적
- Data Modeling, Routing, Ajax 기능없음
- 프레임워크처럼 마법의 지팡이가 아님
- IE8이하 지원 X

## 서버&클라이언트 렌더링
- 둘다 지원한다.
- 보통 클라이언트 렌더링만 되기때문에 Javascript처리가 끝난다음에 UI 렌더링 초기 구동딜레이
- 유저에게 쾌적함을 줄라면 서버에서 HTML생성하고 문자열 형태로 서버렌더링
- 구글 같은 경우에는 검색봇이 Javascript를 실행하나 다른 사이트는 아직 미지원 검색엔진최적화(SEO)를 하기위해 서버렌더링
- 방문자가 많은데 서버컴퓨터 성능이 좋지 않다면 서버렌더링 비추
- 서버컴퓨팅 성능도 좋고 분산처리를 잘 구현했다면 서버렌더링 추천
