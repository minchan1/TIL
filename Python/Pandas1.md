# Pandas



## 판다스란?

- 파이썬에서 사용하는 데이터 전처리용 패키지.
- 엑셀처럼 파일을 다룰 수 있게 해줌.
- 엑셀과는 다르게 1GB 이상의 큰 파일도 빠르게 처리가 가능.
- 더 복잡한 처리와 DB와의 연동과 같은 여러 기능을 제공.



### Series

- 1차원 구조를 표현

- ```python
  series = pd.Series([10, 20, 30, 40])
  series
  0    10
  1    20
  2    30
  3    40
  dtype: int64
  ```

- ```python
  display( series.ndim )
  display( series.shape )
  1
  (4,)
  ```

  



### DataFrame

- 2차원 구조

- 여러개의 시리즈가 모여서 하나의 데이터프레임이 된다.

- ```python
  weight = pd.DataFrame([
  [76.4, 'kg'],
  [75.8, 'kg'],
  [76, 'kg'],
  [76.2, 'kg']])
  ```

- ```python
  weight
  	0	1
  0	76.4	kg
  1	75.7	kg
  2	76.0	kg
  3	76.2	kg
  ```

- ```python
  display( weight.ndim )
  display( weight.shape )
  2
  (4, 2)
  ```

  



### 파일 읽어오기

- 판다스는 read_csv라는 기능으로 파일을 읽어올 수 있다.

- CSV (Comma Seperated Value)

- 텍스트가 콤마로 구분된 형태의 파일

- 엑셀, csv 등의 다양한 파일 형태를 읽어서 데이터프레임 형태로 변환

- ```python
  rawData = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/data/weight_log.csv')
  rawData
  ```



## 데이터 프레임 사용하기



### 출력

- head : 자료의 제일 앞 5개(변경할 수 있음)를 출력

- tail : 자료의 맨 끝 5개를 출력

  ```python
  DataFrame.head(n=5)
  DataFrame.tail(n=5)
  rawData.head(2) # 파라미터를 통해 출력 갯수를 제한
  ```



### 데이터의 요약된 정보

- ```python
  rawData.info()
  <class 'pandas.core.frame.DataFrame'>
  RangeIndex: 9 entries, 0 to 8
  Data columns (total 7 columns):
   #   Column  Non-Null Count  Dtype  
  ---  ------  --------------  -----  
   0   회차      9 non-null      int64  
   1   이름      9 non-null      object 
   2   측정일     9 non-null      object 
   3   몸무게     6 non-null      float64
   4   단위      9 non-null      object 
   5   담당      9 non-null      object 
   6   지점      9 non-null      object 
  dtypes: float64(1), int64(1), object(5)
  memory usage: 632.0+ bytes
  ```

- ```python
  rawData.describe(include='all')
  	   회차	이름	측정일	몸무게	단위	담당	지점
  count	9.000000	9	9	6.000000	9	9	9
  unique	NaN	1	9	NaN	1	3	4
  top	NaN	홍길동	2020-03-04	NaN	kg	김현경	서초구
  freq	NaN	9	1	NaN	9	4	4
  mean	5.000000	NaN	NaN	75.833333	NaN	NaN	NaN
  std	2.738613	NaN	NaN	0.492612	NaN	NaN	NaN
  min	1.000000	NaN	NaN	75.000000	NaN	NaN	NaN
  25%	3.000000	NaN	NaN	75.700000	NaN	NaN	NaN
  50%	5.000000	NaN	NaN	75.850000	NaN	NaN	NaN
  75%	7.000000	NaN	NaN	76.150000	NaN	NaN	NaN
  max	9.000000	NaN	NaN	76.400000	NaN	NaN	NaN
  ```

  



### 인덱싱 (색인)

- 넘파이의 배열 인덱스와 유사
- 판다스의 데이터프레임은 기본적으로 열우선 인덱스



#### 열(column) 인덱싱

- 행을 선택하지 않고, 시리즈를 선택하는 방향으로 인덱싱

- ```python
  rawData['몸무게']
  0    76.4
  1    75.7
  2    76.0
  3     NaN
  4    76.2
  5    75.7
  6     NaN
  7     NaN
  8    75.0
  Name: 몸무게, dtype: float64
  ```

- 배열 인덱스를 지원

- ```python
  col = ['이름', '몸무게', '측정일']
  rawData[col]
  	이름	몸무게	측정일
  0	홍길동	76.4	2020-03-01
  1	홍길동	75.7	2020-03-02
  2	홍길동	76.0	2020-03-03
  3	홍길동	NaN	2020-03-04
  4	홍길동	76.2	2020-03-05
  5	홍길동	75.7	2020-03-06
  6	홍길동	NaN	2020-03-07
  7	홍길동	NaN	2020-03-08
  8	홍길동	75.0	2020-03-09
  ```



#### 행(row) 인덱싱

- loc
- iloc
- 























