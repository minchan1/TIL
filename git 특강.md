# TIL

## Git & Git Hub 01

### Git ?

- 버전 관리 시스템
  - PC로는 용량문제 등 한계가 있음
  - 갱신 내용만 저장하여 효율적으로 관리
- Git Hub를 통해 작업을 공유할 수 있다



### Interface



- 서로 다른 두 개의 시스템이 만나는 접점

- CLI의 진입 장벽이 높아 GUI가 개발

  

### CLI



- Command Line Interface

- Git Bash

  - 윈도우 환경은 개발에 적합하지 않음
  - 개발에 적합한 Linux 환경을 만들어준다 
  - (Unix 계열의 운영체제)

- 기본적인 명령어들

  - `touch` : 파일을 생성

  - `mkdir` : 폴더를 생성

  - `ls` : 현재 경로에 있는 파일과 폴더 리스트를 보여줌

    - -a 를 추가하면 숨겨진 리스트도 보여줌

  - `mv (파일명) (폴더명)` : 파일을 폴더로 옮겨줌

    - 목적지가 없는경우 이름이 변경됨

  - `cd` : 해당 경로로 이동, '..'을 사용하면 상위경로로 이동

  - `rm` : 파일이나 폴더(-r) 삭제

  - `start`,`open` : 파일 열기

    


## git 시작하기





### 프로젝트 초기화시 세팅

```python
$ mkdir pjt
$ cd pjt
  # *** README 파일 & .gitignore 생성 ***
$ touch README.md  .gitignore
  # => gitignore.io에 접속, 필요한내용 복붙
$ git init # => 초기화
$ git config --global user.name '내이름'
$ git config --global user.email 'github에서 쓸 메일주소'
$ cat ~/.gitconfig # => 입력한대로 잘 나오는지 확인
$ git commit -m 'first commit'
 # remote 저장소 생성 @ github.com
 # 생성한 원격 저장소 등록
$ git remote add origin <URL>
 # 지금까지의 commit push 하기
$ git push origin master
```



### 주요 명령어들



- 초기화 시점에 1회 입력

```python
$ git init
```

- 작업하며 계속 입력

```python
$ git add <filename>
$ git commit -m 'MESSAGE'
```

- 모니터링 명령어

```python
$ git status   # 현재 상황
$ git log      # commit 로그
```



### 팁과 정보들

- 리포 (repository) => 저장소 라는 의미
  - master 가 붙은것이 리포

- commit = 버저닝 하는 행동. 스냅샷 이라고도 함
  - git commit -m(남길메시지) '이름'

- 글씨색 구분?
  - 변경사항 있는데 commit 못함 = 빨강
  - 변경사항 있고 commit 가능 = 녹색

- git add .  < 현위치에서 변경사항잇는 모든파일 올라감

- 스테이지의 필요성?? 업무 단위를 묶어서 처리하기 위함



## 주의해야할 행동 ! !

- 홈폴더를 리포로 만들지 않기!! ( ~에서 $ git init 진행)
- 리포안에 리포만들지 않기

- $ git init 입력 전 확인할 점
  - ~ 인지
  - (master) 떠 있는지

- 종종 콜론이 나오고 멈추는경우 q 입력을 통해 탈출가능



## Git Hub 연동하기



### 원격 저장소 (remote repo) 등록하기

```python
$ git remote add origin <URL>
```

### 원격 저장소에 PUSH 하기

```python
$ git push -u origin master
```

### 원격 저장소 확인하기

```python
$ git remote -v
```



