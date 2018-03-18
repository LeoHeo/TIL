## CommonOAuth2Provider
> CommonOAuth2Provider pre-defines a set of default client properties for a number of well known providers: Google, GitHub, Facebook, and Okta.

- spring security 5.0부터 생김
- Google, Facebook, Github and Okta를 기본적으로 제공
- WebSecurityConfigurerAdapter에서 oauth를 쓸라고 하면 `boo-starter-security`말고 아래 디펜던시도 추가

```
compile group: 'org.springframework.security', name: 'spring-security-oauth2-client', version: '5.0.3.RELEASE'
```
