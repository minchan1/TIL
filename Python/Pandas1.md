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

- 슬라이스도 가능

- 판다스의 슬라이스는 마지막 인덱스를 포함한다.

- ```python
  rawData.loc[0:3]
  
  ```

- 행에 대해서 배열 인덱싱

- ```python
  rawData.loc[[1, 3, 5]]
  rawData.reindex([1, 3, 5]) # 같은 기능
  ```



#### 행, 열 인덱싱

- ```python
  rawData.loc[0, '몸무게']
  76.4
  
  # 배열 인덱스와 함께 사용도 가능하다
  rawData.loc[0, ['이름', '몸무게']]
  이름      홍길동
  몸무게    76.4
  Name: 0, dtype: object
          
  # 슬라이스와 함께 사용
  rawData.loc[0:3, ['이름', '몸무게']]
  	이름	몸무게
  0	홍길동	76.4
  1	홍길동	75.7
  2	홍길동	76.0
  3	홍길동	NaN    # 마지막 구간도 포함!
  
  rawData.loc[0:3, '이름':'몸무게']
  이름	측정일	몸무게
  0	홍길동	2020-03-01	76.4
  1	홍길동	2020-03-02	75.7
  2	홍길동	2020-03-03	76.0
  3	홍길동	2020-03-04	NaN
  ```

  

#### loc와 iloc

- iloc를 사용하면 컬럼 인덱스에 정수를 사용할 수 있다

- ```python
  rawData.iloc[0:3, 1:4]
  이름	측정일	몸무게
  0	홍길동	2020-03-01	76.4
  1	홍길동	2020-03-02	75.7
  2	홍길동	2020-03-03	76.0  # 마지막 구간 포함안됨..!
  ```



### 조건 검색

- 불리언 인덱스의 활용

- ```python
  # 불리언 시리즈가 반환된다.
  # 반환된 불리언 시리즈(배열)를 인덱스로 활용!
  rawData['지점'] == '여의도'
  rawData[ rawData['지점'] == '여의도' ]
  
  # 범위도 가능.  ex) 몸무게가 76이상인 자료만 검색?
  rawData[ rawData['몸무게'] >= 76 ]
  ```



#### 다중 조건

- and, or, not

- 판다스는 &(앰퍼샌드), | (파이프라인), ~ (틸드) 문자를 사용

- 우선순위가 헷갈릴 수 있으므로 괄호를 이용해서 정확하게 표현하자

- ```python
  rawData[ (rawData['지점'] == '서초구') & (rawData['담당'] == '최현경') ]
  회차	이름	측정일	몸무게	단위	담당	지점
  5	6	홍길동	2020-03-06	75.7	kg	최현경	서초구
  6	7	홍길동	2020-03-07	NaN	kg	최현경	서초구
  ```



#### 문자열 처리

- ```python
  # isin은 리스트를 파라미터로 갖는다.
  # 리스트 내의 값들 중에서 하나라도 존재하면 True. 그렇지 않으면 False
  rawData[ (rawData['지점'] == '서초구') & (rawData['담당'].isin(['김현경', '최현경'])) ]
  ```

- ```python
  # 담당자들 중에 성이 '김'씨인 자료만 검색?
  
  # contains는 문자열 내에서 특정 문자열이 존재하면 True, 그렇지 않으면 False
  rawData[ rawData['담당'].str.contains('김') ]
  
  # 위 방법은 성이 아닌 이름에 '김'이 포함되는 경우가 있을수 있음
  # starswith 는 문자열 내에서 특정 문자열로 시작하는 경우 True, 그렇지 않으면 False
  rawData[ rawData['담당'].str.startswith('김') ]
  ```



#### 결측치

- 결측치가 있으면 분석을 제대로 수행할 수 없다.

- 따라서 결측치 값을 추가 또는 삭제 처리를 해야함

- 평균, 중앙값 등으로 대체하기도 한다

- ```python
  # 결측치를 확인하는 방법
  rawData['몸무게'].isnull()
  rawData['몸무게'].isna()
  
  # True는 1과 같기 때문에, 모두 더하면 결측치의 갯수가 된다
  rawData['몸무게'].isna().sum() 
  ```

- ```python
  # 결측치만 확인하고 싶다면?
  rawData[ rawdata['몸무게'].isna() ]
  
  # 제외하고 확인하려면?
  rawData[ ~rawdata['몸무게'].isna() ]
  rawData[ rawdata['몸무게'].notna() ]
  ```

- ```python
  # 조건에 맞는 자료들 중에서 내가 원하는 컬럼만 확인
  rawData.loc[ rawData['몸무게'].isna(), '이름' ]
  rawData.loc[ rawData['몸무게'].isna(), ['지점', '담당', '측정일'] ]
  ```



#### 이상치(outlier)

- 특별히 크거나, 작은 값

- 얼마나 크거나 작아야 하는가? => 정해져 있지는 않다. 분석가의 재량

- 이상치를 찾는 경우가 아니면 제거하고 분석을 진행

- ```python
  rawData['몸무게'].describe()
  count     6.000000
  mean     75.833333
  std       0.492612
  min      75.000000
  25%      75.700000
  50%      75.850000
  75%      76.150000
  max      76.400000
  Name: 몸무게, dtype: float64
  ```

- ```python
  # 특정 값을 넘어가는 자료를 이상치로 판단한다면
  rawData[ rawData['몸무게'] > 76.15 ]
  
  # 4분위수를 이용한 방법
  rawData['몸무게'].sort_values()
  display( rawData['몸무게'].quantile(0.25) )
  display( rawData['몸무게'].quantile(0.50) )
  display( rawData['몸무게'].quantile(0.75) )
  
  # 특정 구간을 이상치로 보고 제거한다면
  low = rawData['몸무게'].quantile(0.01)
  high = rawData['몸무게'].quantile(0.99)
  rawData[ (rawData['몸무게'] < high) & (rawData['몸무게'] > low) ]                             
  ```



#### 중복 데이터 검사

- duplicated를 이용해서 중복된 자료를 검사

- ```python
  rawData.duplicated(subset=['지점'])
  0    False
  1     True
  2    False
  3     True
  4    False
  5    False
  6     True
  7     True
  8     True
  dtype: bool
  ```

- ```python
  rawData[ rawData.duplicated(subset=['지점'], keep=False) ]
  
  	회차	이름	측정일	몸무게	단위	담당	지점
  0	1	홍길동	2020-03-01	76.4	kg	박현경	관악구
  1	2	홍길동	2020-03-02	75.7	kg	김현경	관악구
  2	3	홍길동	2020-03-03	76.0	kg	최현경	여의도
  3	4	홍길동	2020-03-04	NaN	kg	최현경	여의도
  5	6	홍길동	2020-03-06	75.7	kg	최현경	서초구
  6	7	홍길동	2020-03-07	NaN	kg	최현경	서초구
  7	8	홍길동	2020-03-08	NaN	kg	김현경	서초구
  8	9	홍길동	2020-03-09	75.0	kg	김현경	서초구
  ```



### 통계 분석



#### pivot

- ```python
  # 지점별 몸무게 평균
  pd.pivot_table( rawData, index='지점', values='몸무게')
  
  # 지점별 몸무게 총합
  pd.pivot_table( rawData, index='지점', values='몸무게', aggfunc=np.sum)
  
  # 지점별 담당자별 몸무게의 평균
  pd.pivot_table( rawData, index=['지점', '담당'], values='몸무게')
  ```



#### crosstab

- ```python
  # 지점별 담당자별 몸무게의 평균
  pd.crosstab( index=rawData['지점'], columns=rawData['담당'], values=rawData['몸무게'], aggfunc=np.mean)
  
  # pivot과 비교해보기
  ```



#### 그룹화

- ```python
  # 그룹화를 통한 통계적 수치
  # 그룹 객체를 반환
  rawData.groupby(['지점'])
  
  # 그룹화를 통한 지점별 몸무게 평균
  rawData.groupby(['지점'])['몸무게'].mean()
  
  # 지점별 담당별 몸무게 평균
  rawData.groupby(['지점', '담당'])[['몸무게']].mean()
  
  # 컬럼별로 집계를 다르게 하고 싶다면
  rawData.groupby('지점').agg({
    '몸무게': 'mean', '담당': 'count'
  })
  ```

- 



## 데이터 프레임 조작하기



### 컬럼의 추가와 수정

- 데이터 프레임이 컬럼이 존재하지 않으면 새로 생성

- ```python
  rawData['지역'] = '서울'
  
  # 해당 컬럼이 존재하는 경우에는 수정이 된다
  rawData['지역'] = 'Seoul'
  ```

- 조건에 맞는 컬럼 생성하기

- ```python
  rawData.loc[ rawData['몸무게'] >= 76, '상태'] = '비만'
  rawData.loc[ rawData['몸무게'] < 76, '상태'] = '정상'
  ```



### 컬럼의 삭제

- 삭제는 신중하게 진행하며, 가급적 원본 데이터는 삭제하지 말자

- ```python
  # drop을 이용해 특정 컬럼을 삭제할 수 있다.
  # drop을 사용하는 경우 특정 컬럼이 삭제된 새로운 데이터프레임을 반환
  rawData.drop(columns=['지역'])
  	회차	이름	측정일	몸무게	단위	담당	지점	상태
  0	1	홍길동	2020-03-01	76.4	kg	박현경	관악구	비만
  1	2	홍길동	2020-03-02	75.7	kg	김현경	관악구	정상
  2	3	홍길동	2020-03-03	76.0	kg	최현경	여의도	비만
  3	4	홍길동	2020-03-04	NaN	kg	최현경	여의도	NaN
  4	5	홍길동	2020-03-05	76.2	kg	김현경	강남구	비만
  5	6	홍길동	2020-03-06	75.7	kg	최현경	서초구	정상
  6	7	홍길동	2020-03-07	NaN	kg	최현경	서초구	NaN
  7	8	홍길동	2020-03-08	NaN	kg	김현경	서초구	NaN
  8	9	홍길동	2020-03-09	75.0	kg	김현경	서초구	정상
  
  # 이 때, 원본은 바뀌지 않는다
  rawData
  	회차	이름	측정일	몸무게	단위	담당	지점	지역	상태
  0	1	홍길동	2020-03-01	76.4	kg	박현경	관악구	Seoul	비만
  1	2	홍길동	2020-03-02	75.7	kg	김현경	관악구	Seoul	정상
  2	3	홍길동	2020-03-03	76.0	kg	최현경	여의도	Seoul	비만
  3	4	홍길동	2020-03-04	NaN	kg	최현경	여의도	Seoul	NaN
  4	5	홍길동	2020-03-05	76.2	kg	김현경	강남구	Seoul	비만
  5	6	홍길동	2020-03-06	75.7	kg	최현경	서초구	Seoul	정상
  6	7	홍길동	2020-03-07	NaN	kg	최현경	서초구	Seoul	NaN
  7	8	홍길동	2020-03-08	NaN	kg	김현경	서초구	Seoul	NaN
  8	9	홍길동	2020-03-09	75.0	kg	김현경	서초구	Seoul	정상
  
  # 원본에서 바로 삭제하는 방법?
  # 따로 반환되지는 않는다
  rawData.drop(columns=['지역'], inplace=True)
  # inplace 파라미터를 True로 하면, 해당 데이터프레임에서 바로 삭제
  
  ```



### 행 추가와 수정, 삭제

- 행이 존재하지 않으면 추가

- ```python
  rawData.loc[9] = [10, '홍길동', '2020-03-10', 77, 'kg', '박현경', '관악구', '비만']
  rawData
  	회차	이름	측정일	몸무게	단위	담당	지점	상태
  0	1	홍길동	2020-03-01	76.4	kg	박현경	관악구	비만
  1	2	홍길동	2020-03-02	75.7	kg	김현경	관악구	정상
  2	3	홍길동	2020-03-03	76.0	kg	최현경	여의도	비만
  3	4	홍길동	2020-03-04	NaN	kg	최현경	여의도	NaN
  4	5	홍길동	2020-03-05	76.2	kg	김현경	강남구	비만
  5	6	홍길동	2020-03-06	75.7	kg	최현경	서초구	정상
  6	7	홍길동	2020-03-07	NaN	kg	최현경	서초구	NaN
  7	8	홍길동	2020-03-08	NaN	kg	김현경	서초구	NaN
  8	9	홍길동	2020-03-09	75.0	kg	김현경	서초구	정상
  9	10	홍길동	2020-03-10	77.0	kg	박현경	관악구	비만
  ```

- 삭제는 컬럼과 마찬가지로 drop을 동일하게 사용

- 파라미터를 columns이 아닌 index 파라미터를 사용

- ```python
  rawData.drop(index=[0, 1, 2])  # 원본 삭제하고 싶으면 inplace 사용가능
  	회차	이름	측정일	몸무게	단위	담당	지점	상태
  3	4	홍길동	2020-03-04	NaN	kg	최현경	여의도	NaN
  4	5	홍길동	2020-03-05	76.2	kg	김현경	강남구	비만
  5	6	홍길동	2020-03-06	75.7	kg	최현경	서초구	정상
  6	7	홍길동	2020-03-07	NaN	kg	최현경	서초구	NaN
  7	8	홍길동	2020-03-08	NaN	kg	김현경	서초구	NaN
  8	9	홍길동	2020-03-09	75.0	kg	김현경	서초구	정상
  9	10	홍길동	2020-03-10	77.0	kg	박현경	관악구	비만	
  ```



#### apply

- 판다스에서 사용 가능한 반복문

- 모든 행과 열에 대해서 동일한 함수를 반복적으로 적용

- ```python
  def func(x) :
      print('함수가 호출되었습니다.')
      print('x : {}'.format(x))
      
      # apply를 통해서 호출되는 함수는 return을 꼭 작성해주자
  
  rawData.apply( func )
  # 기본적으로 데이터프레임의 각 컬럼들이 시리즈 형태로 전달
  
  # 컬럼이 아닌 행을 전달하고 싶다면
  def func(x) :
      print('함수가 호출되었습니다.')
      print('x : {}'.format(x))
      
  rawData.apply( func, axis=1 )
  ```

- ```python
  # 지점별로 새로운 지역을 만들어 본다면
  def func(x) :
      if x['지점'] == '관악구' : return '강서'
      elif x['지점'] == '여의도' : return '강서'
      elif x['지점'] == '강남구' : return '강동'
      elif x['지점'] == '서초구' : return '강동'
      
  rawData.apply(func,axis=1)
  0    강서
  1    강서
  2    강서
  3    강서
  4    강동
  5    강동
  6    강동
  7    강동
  8    강동
  9    강서
  dtype: object  # apply가 리턴하는 값들도 하나의 시리즈가 된다.
  ```

- ```python
  # 이를 이용해서 새로운 컬럼을 추가한다면
  rawData['지역'] = rawData.apply(func,axis=1)
  ```



### 프레임 합치기

- 여러 소스로부터 가져온 데이터를 분석하려면 하나의 데이터프레임 이어야 한다
- 서로 다른 두 자료를 하나의 데이터 프레임으로 합치는 것



#### inner join

- merge 함수를 통해서 'join'을 해볼 수 있다

- merge의 기본 동작은 'inner join'

- 자료의 크기가 줄어들게 된다

- ```python
  display(len(user_device))
  display(len(user_usage))
  272
  240
  
  pd.merge(left=user_usage, right=user_device, on='use_id')
  ```



#### left join

- left 자료를 기준으로 합쳐준다

- right에 없는 자료는 결측치로 채워진다

- ```python
  # how에 어떻게 join할지 입력하면됨
  pd.merge(left=user_usage, right=user_device, on='use_id', how='left')
  
  # right join도 같은 원리
  ```



#### full outer join

- ```python
  pd.merge(left=user_usage, right=user_device, on='use_id', how='outer')
  ```



#### 결론

- 데이터 전처리 작업의 핵심은 합치고 나누고 붙이고 자르는 작업
- 이 작업을 반복하는 과정





































