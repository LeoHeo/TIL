# Git?

---

# CVCS VS DVCS

CVCS(Concurrent Version Control System) - CVS, Subversion, Perforce

DVCS(Distributed Version Control Sytem) - Git, Mecurial, Mecurial

## 무슨말이야? 그림으로 확인해보자

---

![fit](http://image.slidesharecdn.com/git-150718063306-lva1-app6892/95/git-13-638.jpg?cb=1437201255)

---

## CVCS 문제점
- 중앙 서버에 발생한 문제
- 만약 서버가 한 시간 동안 다운되면 그동안 아무도 다른 사람과 협업할 수 없고 사람들이 하는 일을 백업할 방법도 없다.
- 중앙 데이터베이스가 있는 하드디스크에 문제가 생기면 프로젝트의 모든 히스토리를 잃는다

---

![fit](http://image.slidesharecdn.com/git-150718063306-lva1-app6892/95/git-14-638.jpg?cb=1437201255)

---

## Git의 역사
- Linux 커널 BitKeeper DVCS 사용
- *2005년에 커뮤니티가 만드는 Linux 커널과 이익을 추구하는 회사가 개발한 BitKeeper의 관계는 틀어졌다. BitKeeper의 무료 사용이 제고된 것*
- 그래서 리누스 토발즈가 만듬(~~이 사람 못하는게 없네~~)

---

## 강의 목표
- 지역저장소와 원격저장소 이해
- CLI(Command Line Interface) 사용법 숙지
- git의 꽃 branch에 대해서 알아보고 이해
- branch 전략들을 알아보고 git-flow이해

---

![fit](http://image.slidesharecdn.com/git-130122191552-phpapp01/95/git-8-638.jpg?cb=1392000829)

---

## Git의 무결성

- Git은 데이터를 저장하기 전에 항상 체크섬을 구하고 그 체크섬으로 데이터를 관리
- SHA-1 해시를 사용하여 체크섬을 만든다. 만든 체크섬은 40자 길이의 16진수 문자열

```sh
24b9da6552252987aa493b52f8696cd6d3b00373
```

---

![fit](https://git-scm.com/book/en/v2/book/01-introduction/images/areas.png)

---

## 세팅먼저 하자

- [ssh세팅](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [github ssh 세팅](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)

```
ssh -T git@github.com
```

---
## Basic Command
- init
- add
- commit
- push

---

## Advanced Command
[git-level-2](http://www.slideshare.net/ibare/git-level-2)

---

## Vincent Driessen가 제안한 git 브랜치 전략
![left fit](http://nvie.com/img/git-model@2x.png)