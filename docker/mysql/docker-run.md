## local에서 mysql Docker 실행방법

- `docker-compose up -d`로 docker를 띄운다.
- `jdbc:mysql://localhost:3306/{db}`명으로 IDE에서 불러온다.

## mysql bash 접근방법
- `docker exec -it {mysql_container_name} bash`
- `mysql -u root -p` -> `secret(docker-compose.yml에 적힌 대로)`
