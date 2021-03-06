# Numpy 01





## Numpy ?

- 수치 해석용으로 만들어진 모듈

- 머신러닝, 딥러닝 에서도 사용됨

- 수치 계산을 위해 만든 라이브러리

- ```python
  # 일반적으로 np로 줄여서 사용한다
  import numpy as np
  ```



## 지원하는 타입

1. array (배열)
   - 통계분석, ML/DL에서 사용
   - 배열 이라고 하며, 파이썬의 리스트와는 다름
2. matrix
   - 수학적 계산이 필요한 경우



### 배열의 기본속성

- ndim : 배열의 차원(dimensions)
- shape : 배열의 크기(= 원소의 갯수)
- 1차원 배열은 행이 1개이고, 열이 n개인 배열을 의미한다.
- 배열의 모양은 튜플로 표현된다.



#### 1차원 배열

- 파이썬의 리스트와 유사함

- ```python
  arr1D = np.array([1, 2, 3, 4])
  arr1D
  array([1, 2, 3, 4])
  ```

- 자료가 몇 차원인지 잘 확인하자!

- 라이브러리, 알고리즘을 이용할 때 중요함.

  

#### 2차원 배열

- 앞으로 주로 다루게 되는 배열은 2차원이다.

- 리스트처럼 배열의 원소로 또다른 배열을 갖는 배열

- ```python
  arr2D = np.array([
  	[1, 2, 3,],
  	[4, 5, 6,],
  	[7, 8, 9,]])
  ```



## 배열의 특징

- 인덱싱, 슬라이싱
- 팬시 인덱싱
- 배열의 타입
- numpy에서만 정의되는 특별한 타입



### 인덱싱, 슬라이싱

- 기본적인 개념은 리스트와 같다.

- 표현이 달라짐

- ```python
  # 1차원 배열은 리스트와 유사함
  display( arr1D )
  array([1, 2, 3, 4])
  
  # 배열도 이터레이블 객체
  for x in arr1D :
      print(x)
      
  # 내장함수도 사용 가능
  display( min( arr1D ))
  display( max( arr1D ))
  
  # 슬라이스도 리스트와 동일하게 사용
  display( arr1D[:] )
  display( arr1D[::-1])
  
  ```



#### 2차원 배열

- 인덱싱은 다음과 같이 표현된다.

- ```
  array[행,열]
  ```

- 슬라이스는 행과 열을 각각 정의할 수 있다.

- ```
  array[행시작:행끝,열시작:열끝]
  ```



### 팬시 인덱싱









