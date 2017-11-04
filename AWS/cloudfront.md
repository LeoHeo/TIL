## CloudFront에서 Custom SSL Certificate 발급
cloudfront에서 https를 사용한다는 전제하에 `CNAME을 걸면 cloudfront에서 자체 발급하는 인증서를 사용할 수가 없음`
그래서 CNAME으로 연결된 주소로 접속하면 위에같은 신뢰할 수 없는 인증서라고 나옵니다.

그래서 `Amazon Certificate Manager 줄여서 ACM에서 Custom SSL Certificate를 발급`해야 하는데
Custom SSL Certificate를 발급받기 위해서는 Seoul region이 아닌 `N.Virginia region에서만 발급`을 받아야 합니다.
