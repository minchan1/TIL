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

  









