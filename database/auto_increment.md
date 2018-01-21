## DB_Sharding시 Auto_increment 문제
- PK가 auto_increment라면 DB Sharding을 할 때 문제가 된다.

```
A_DB - 100번
B_DB - 100번

서로 유니크 하지가 않음
```

## 해결방법
- uid를 사용한다.
