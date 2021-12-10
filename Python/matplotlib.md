# matplotlib



## 시각화

- 자료분석의 기본은 통계와 그래프

- 수치를 통한 자료 이해  -> 통계

- 자료에 대한 직관적인 이해 -> 시각화

  

### 파이썬에서의 시각화

- matplotlib
  - 가장 기본적인 시각화 라이브러리
  - 파이썬에서 제공하는 대부분의 라이브러리들의 기반

- seaborn
  - matplotlib을 기반으로 만들어진 라이브러리
  - 자료의 시각화
- plotly
  - 사용하기 편하며 3차원 그래프도 그릴수있음
  - 회전, 확대, 클릭 등 인터랙티브한 사용 가능
  - 느리고 무겁다는 단점



### 한글화

- matplotlib은 한글을 지원하지 않음

- 폰트를 바꿔주어야 함

- colab에서는 매번 바꿔야한다..

- ```python
  # 폰트 설정을 위한 라이브러리 임포트
  from matplotlib import font_manager,  rcParams
  
  # 한글 표현이 가능한 폰트를 설치
  !apt-get install fonts-nanum*
  
    ## 설치된 폰트를 확인
  font_manager.findSystemFonts(fontext='ttf')
  
    ## 설치된 폰트의 이름 확인
  font_manager.FontProperties( fname='/usr/share/fonts/truetype/nanum/NanumGothicCoding.ttf').get_name()
  
  # 폰트 설정
  rcParams['font.family'] = 'NanumGothicCoding'
  rcParams['axes.unicode_minus'] = False
  font_manager._rebuild()
  ```

-  colab 환경에서의 설정 전체 코드

- 아래의 명령을 실행한 후

- 런타임 -> 다시시작 및 모두실행 을 클릭, 모든 셀의 명령을 다시실행

- ```python
  from matplotlib import font_manager, rcParams
  !apt-get install fonts-nanum*
  rcParams['font.family'] = 'NanumGothicCoding'
  rcParams['axes.unicode_minus'] = False
  font_manager._rebuild()
  ```

  

## 그래프를 그리는 기준

1. 자료의 형태 (변수의 종류)
   - 범주형과 연속형 자료로 구분
   - 질적변수 : 변수의 값이 비 수치적, 특정 카테고리에 포함
     - 명목형 : 특정 범주에 포함되지만, 순위는 갖지않음 (성별, 혈액형 등)
     - 순위형 : 특정 범주에 포함되며 순위를 가짐(성적, 등급 등)
   - 양적변수 : 변수의 값이 수치적, 연속적(키, 나이 등)
     - 이산형 : 셀 수 있는 경우(정수) 
     - 연속형 : 셀 수 없는 경우(실수)     # 예외가 있을 수 있음



2. 자료의 차원
   - 변수의 갯수가 차원이 됨
   - 차원이 높으면 시각화 하기 어려움
   - 최대 2차원의 화면에서  3차원까지 나타낼 수 있다
   - 1차원
     - 일변수(일변량) : 변수 하나에 대한 시각화
     - 변수의 분포 등을 확인
   - 2차원
     - 이변수(이변량) : 변수와 변수의 관계를 확인하고 싶은 경우
     - 연속형 변수와 연속형 변수
     - 연속형 변수와 이산형 변수
     - 이산형 변수와 이산형 변수



### 1차원 시각화

- 변수 1개인 경우
  - 범주형 : countplot (빈도 확인)
  - 연속형 : histplot, displot, barplot



#### 범주형

- 샘플 자료에서는 비수치적인 자료는 없음

- 수치적인 자료들 (이산형) 중에서 범주형에 해당하는 변수 확인

- ex) 흡연상태, 검진여부, 성별코드 등

- ```python
  rawData['흡연상태'].unique()
  array([3., 1., 2.])
  
  sns.countplot(data=rawData, x='흡연상태')
  sns.countplot(data=rawData, x='성별코드')
  ```



#### 이산형

- 셀 수 있는 형태의 정수자료



#### 연속형







### 2차원 시각화

- 두 자료간의 관계를 확인하고 싶은 경우
  - 타겟변수와 입력변수들 사이의 관계 (인과성)
  - 입력변수와 입력변수들 사이의 관계 (상관성)
  - 입력변수들은 서로 독립적임을 가정



- 두 변수 모두 연속형
  - scatterplot, lineplot, jointplot, rugplot, ...
- 연속형 변수와 범주형 변수
  - barplot, boxplot
- 두 변수 모두 범주형
  - countplot



#### 두 변수 모두 연속형

- ```python
  # 산포도
  sns.scatterplot(data=rawData, x='총콜레스테롤', y='트리글리세라이드')
  
  # 상관계수?
  rawData[['총콜레스테롤', '트리글리세라이드']].corr()
  ```

- rugplot은 자료의 위치정도를 확인할 수 있다.

- 밀도를 파악할 수 있음



#### 파생변수 ?

- 주어진 자료에서 타겟변수를 가장 잘 설명할 수 있는

- 새로운 변수를 만들어 내는 것 = > 데이터 마이닝

- IDL = 총콜레스테롤 - (HDL + LDL)

- ```
  
  ```

- 

  

#### 연속형 변수와 범주형 변수

- barplot (비율)

- boxplot
  - 4분위수를 이용한 시각화
  - 이상치(outlier)를 확인하는 용도로 사용
  - 1분위수 : 자료의 25%에 해당하는 값
  - 2분위수 : 자료의 50%에 해당하는 값 (중앙값과 동일)
  - 3분위수 : 자료의 75%에 해당하는 값



#### 두 변수 모두 범주형

- ```python
  sns.countplot(data=rawData_without_outlier, x='성별코드', hue='흡연상태')
  ```

- 





### 변수가 3개 이상

- ```python
  sns.barplot(data=rawData_without_outlier, x='흡연상태', y='IDL콜레스테롤', hue='성별코드')
  
  ```

- 





## 그래프 표현



### 레이아웃 분할



### 색상 지정

- 

