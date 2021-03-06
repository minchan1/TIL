# 파이썬 정리하기



## 자료형

- 숫자, 문자열 등 자료 형태로 사용하는 모든 것.
- 프로그램의 기본이자 핵심 단위가 된다.
- 프로그래밍 언어의 자료형을 알고 이해하는것이 핵심!



### 숫자형

- 숫자형의 사용법

  1. 정수형(integer) : 양의 정수, 음의 정수, 0

     ```python
     >>> a = 100
     >>> a = -50
     >>> a = 0
     ```

  2. 실수형(float) : 소수점이 포함된 숫자

     ```python
     >>> a = 1.25
     >>> a = -2.44
     ```

  3. 8진수, 16진수 : 0o, 0x로 시작

     ```python
     >>> a = 0o123
     >>> a = 0xABC
     ```

     

- 연산자

  1.  사칙연산 (+, -, *, /)

     ```python
     >>> a = 3
     >>> b = 4
     >>> a + b
     7
     >>> a * b
     12
     >>> a / b
     0.75
     ```

  2. x의 y제곱 (**)

     ```python
     >>> a = 3
     >>> b = 4
     >>> a ** b
     81
     ```

  3. 나머지를 반환 (%)

     ```python
     >>> 7 % 3
     1
     >>> 3 % 7
     3
     ```

  4. 몫을 반환 (//)

     ```python
     >>> 7 // 4
     1
     ```



### 문자열 자료형

- 문자, 단어 등으로 구성된 문자들의 집합

- 문자열의 사용법

  1. 큰따옴표( " ) , 작은따옴표( ' ) 로 둘러싸기
  2. 큰따옴표, 작은따옴표 3개를 연속으로 둘러싸기

- 문자열 안에 따옴표 포함시키기

  1. 문자열에 포함되지 않은 따옴표로 둘러싸기
  2. 백슬래시를 사용해서 포함시키기 (문자열 이스케이프)

- 여러 줄인 문자열을 변수에 대입하기

  1. 이스케이프 코드 \n 삽입하기
  2. 연속된 따옴표 3개 사용하기

- 문자열 연산하기

  1. 문자열 더해서 연결하기
  
     ```python
     >>> head = "Python"
     >>> tail = " is fun!"
     >>> head + tail
     'Python is fun!'
     ```
  
  2. 문자열 곱하기
  
     ```python
     >>> a = "python"
     >>> a * 2
     'pythonpython'
     ```
  
  3. 문자열 길이 구하기
  
     ```python
     >>> a = "Life is too short"
     >>> len(a)
     17
     ```



### 인덱싱과 슬라이싱

- 인덱싱(indexing)이란 무엇인가를 가리킨다는 의미

- 슬라이싱(Slicing)은 무엇인가를 잘라낸다는 의미

- 파이썬은 숫자를 0부터 센다.

  ```python
  >>> a = "Life is too short, You need Python"
  >>> a[3]
  'e'  # 0부터 시작
  a[0]:'L', a[1]:'i', a[2]:'f', a[3]:'e', a[4]:' ', ...
  ```

- 문자열을 뒤에서부터 읽을때는 마이너스(-) 기호

  ```python
  >>> a[-2]
  'o'
  >>> a[-5]
  'y'
  ```

- 문자열 슬라이싱의 활용?

  ```python
  >>> a = "Life is too short, You need Python"
  >>> b = a[0] + a[1] + a[2] + a[3]
  >>> b
  'Life'
  >>> a[0:4] # 끝번호는 포함하지 않는다.
  'Life'
  ```

  











