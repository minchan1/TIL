# 장고 설치

- 교재(p.87) 2.3.3 Django 설치하기

- VScode 에서는

  - 파이썬 파일을 선택한 이후 인터프리터를 설치한 가상환경 선택
  - 터미널 실행 후 다음과 같이 보여져야 한다

- ```
  Microsoft Windows [Version 10.0.18362.959]
  (c) 2019 Microsoft Corporation. All rights reserved.
  
  C:\IJH\workspace>C:/ProgramData/Anaconda3/Scripts/activate
  
  (base) C:\IJH\workspace>conda activate multicampus
  
  (multicampus) C:\IJH\workspace>
  -------------
  가상환경이 선택된 이후에 명령어를 실행을 해야함
  ```





## 터미널에서 가상환경 선택

- 가상환경 목록 확인

- ```
  (minchan1) C:\Users\alfls\workspace>conda env list
  가상환경 목록 확인 명령어
  
  # conda environments:
  #
  base                     C:\ProgramData\Anaconda3
  minchan1              *  C:\Users\alfls\.conda\envs\minchan1
  -------            -----  ---------------------------------
  가상환경 이름     현재 선택된 환경   가상환경이 설치된 경로
  ```

- 가상환경 선택

- ```
  (minchan1) C:\Users\alfls\workspace>conda activate minchan1
  ```

- 주의

  - 설치는 명령어 기반이기 때문에 명령어를 실행할 때의 가상환경이 중요
  - 다른 가상환경에 설치되지 않도록 주의



## 파이썬 모듈 (패키지) 설치

- 어떤걸 사용해도 문제 x
  1. pip
  2. conda



### pip를 이용한 패키지 관리

- ```
  # 설치된 모듈(패키지) 확인
  prompt> pip list
  
  # pip를 이용한 설치
  prompt> pip install [설치할 모듈(패키지) 이름]
  
  # pip를 이용한 모듈(패키지) 업그레이드
  prompt> pip install --upgrade [업그레이드할 모듈(패키지) 이름]
  ```



### conda를 이용한 패키지 관리

- ```
  # 설치된 모듈(패키지) 확인
  prompt> conda list
  
  # 설치
  prompt> conda install [설치할 모듈(패키지) 이름]
  ```



## 장고 설치

- pip 업그레이드

  - pip는 파이썬의 패키지 관리자이다
  - 항상 최신버전으로 유지해주는게 좋다
  - 명령어가 update가 아닌 upgrade 라는것에 주의
  - 권한 문제가 발생할 수 있지만 설치에는 문제가 없음

- ```
  # pip 업그레이드
  prompt> pip install --upgrade pip
  
  # 장고 설치
  prompt> pip install django
  
  # 설치 확인
  prompt> pip list
  ...
  django
  ...
  # 목록에서 django 이름이 보이면 된다
  ```

  

# 장고 예제 따라해보기



## 프로젝트 생성

- 하나의 웹 사이트를 만들려면 하나의 프로젝트를 생성

- 교재 p.90

  - 교재의 첫번째 프로젝트 이름은 ToDoList

- 프로젝트 생성하는 방법

- ```
  prompt> django-admin startproject 프로젝트이름
  ```

  

### 프로젝트에서 생성되는 것들

- ```
  프로젝트/
    - manage.py
    - 프로젝트/
      - __init__.py
      - setting.py
      - urls.py
      - wsgi.py
      - asgi.py
  ```

- manage.py

  - 전체적인 프로젝트를 관리할 수 있는 유틸
  - 프로젝트 초기화, 마이그레이션, 앱 생성 등

- 프로젝트/setting.py

  - 현재 프로젝트의 환경설정 파일

- 프로젝트/urls.py

  - 현재 프로젝트의 URL에 대한 설정

- 프로젝트/wsgi, asgi.py

  - 작성된 웹 사이트를 서버를 통해서 배포하는 경우에 사용
  - 수업 시간에는 로컬 환경에서만 동작 확인





## 가상서버 실행

- ```
  prompt> cd 프로젝트폴더
  prompt> python manage.py runserver
  ```





## 앱 생성하기

- 앱(app/application)

- 하나의 프로젝트는 여러개의 앱으로 구성

- 기능 또는 서비스에 따라서 여러개의 앱을 구성

  - 현재 진행하는 프로젝트는 하나의 앱으로 구성됨
  - ToDoList 프로젝트는 할일목록 기능만 있는 것

- 앱 생성하는 방법

  - 교재에서 사용하는 앱의 이름은 my_to_do_app

- ```
  prompt> python manage.py startapp 앱이름
  ```

  



## MVC 구조

- 웹 프레임워크
  - 웹 서비스를 하기 위해 필요한 구조를 제어하기 편하게 미리 만들어 놓은 구조
  - 프레임워크에서 제공하는 구성에 맞춰서 작성만 하면 서비스가능
- MVC
  - Model, View, Control의 약자
  - 기능별로 프레임워크 구조가 나눠져 있다
  - 각각의 역할을 이해하고 그에 맞춰 기능을 구현
  - Model
    - DB와 관련된 기능
    - 장고에서는 `models.py`가 해당 역할을 수행
  - View
    - 화면에 보여지는 기능
    - 장고에서는 `Templates`를 이용해서 view 역할을 수행
  - Control
    - View와 Model 사이의 제어 역할
    - 장고에서는 `views.py`가 해당 역할을 수행
- 장고는 다른의미로 MVT 구조라고 하기도 함



## 템플릿 작성하기

- 교재(p.134) 1.4 HTML 템플릿 사용하기

- `view`를 담당하는 기능

  - 사용자에게 보여지는 기능
  - HTML 소스코드를 브라우저에 보여질 수 있게 하는 기능

- `templates`폴더는 `앱폴더`에 직접 폴더를 만들어주면 됨

  - 장고는 `templates`폴더에서 찾게 됨
  - `templates` 폴더에 앱이름과 동일하게 폴더를 하나 더 생성

- 실제 폴더의 구조는 다음과 같다

- ```
  프로젝트폴더/
   - manage.py
   - 프로젝트폴더/
   - 앱폴더/
     -templates/
       -앱폴더/
  ```

- 해당 앱에서 화면에 보여지는 내용이 있다면 `templates`폴더를 찾게 되고

  - `templates`폴더 내에서 앱이름과 동일한 이름의 폴더를 찾아서
  - 그 내부에 있는 HTML 파일을 사용하게 됨





## 앱등록

- 장고에서는 앱을 사용하려면 설정에서 해당 앱을 등록해줘야 함

  - `setting.py`에서 설정함
  - 추가를 해주지 않으면 장고는 어떤 앱이 설치되었는지 알 수 없음

- `프로젝트폴더/프로젝트폴더/settings.py`

  - `INSTALLED_APPS`를 찾아서 추가된 앱을 리스트에 등록

- ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  
  # 설치된 앱을 등록해준다
  INSTALLED_APPS += [
      'my_to_do_app',
  ]
  ```

  





## URL 설정

- 교재(p.127) 1.3 URL 설정하기

- 뷰(templates)를 호출하려면 연결을 해줘야 한다

  - `urls.py`이 URL을 연결해주는 역할을 함
  - 우리가만든 `index.html`과 `url`을 연결

- 최상위 `URLconf`에서 요청하는 URL과 앱을 먼저 연결하기

  - `프로젝트폴더/프로젝트폴더/urls.py`
  - 최상위 `URLconf`에서 담당하는 역할은 다음과 같음

- ```
  http://1247.0.0.1:8000/         admin/index.html
  ----------------------          ----------------
  네트워크에서 서버의 경로        서버에서 해당 폴더/파일의 경로
  ```

- `path`는 URL과 앱을 연결해주는 라우팅 함수이다

  - 필수인자 2개
  - path(route,view)
  - route는 URL 패턴을 가진 문자열이 됨
    - 문자열에 해당하는 앱 또는 뷰와 연결 가능
  - view는 route에서 일치하는 패턴을 찾으면 view함수를 호출
    - include()와 같은 경우 하위 `URLconf`에 대한 설정을 호출





### 하위 URLconf

- 최상위 URLconf로부터 연결이 설정되었다면 해당 앱에서는 따로 urls.py를 만들어 주면 됨 (앱폴더에)
  - 프로젝트폴더/앱폴더/urls.py 를 생성

- urls.py는 다음과 같이 작성

- ```
  from django.urls import path, include
  # view와 연결
  from . import views
  
  urlpatterns = [
    # 해당 url 패턴을 views.py의 index 함수와 연결
    path('', views.index),
  ]
  ```

  



## 뷰 작성하기

- 장고에서 뷰는 제어 역할을 함

  - `URL`과 `템플릿`
  - `템플릿`과 `모델` 등의 연결 역할을 해줌
  - 가장 많이 사용하게되는 모델

- index 함수의 정의

- ```
  def index( request ):
    return render(request, 'my_to_do_app/index.html')
  ```

  

## 디비 설정

- 교재 p.143~
- 웹 브라우저로부터 `할 일`을 전달 받아서 `DB`에 저장
  - SQL Query를 사용하지 않고도 사용할 수 있다 (ORM)
- 교재의 예제는 `sqlite3`를 사용하고 있음
  - 장고의 기본 `DBMS(DataBase Management System)`는 `sqlite3`이기 때문에 추가적인 설치나 설정은 필요하지 않음



## 모델 만들기

- MVC 구조에서 `M(Model)`에 해당하는 내용
- 장고에서 모델은 `models.py`로 작성 가능
  - 모델은 자료를 저장할 `테이블`이라고 보면 된다
  - `테이블`은 판다스의 `DataFrame`과 동일한 개념이다
  - 할 일을 저장할 `테이블`을 `models.py`를 통해서 만들어 보자



### 모델의 형태

- 모델의 형태는 테이블의 형태가 된다

  - ToDo에 대한 데이터를 다루기 때문에 ToDo를 저장할 테이블만 있으면 된다
  - 컬럼이 하나이고 이름이 `ToDo`인 데이터프레임과 동일한 모양

- 장고에서는 데이터베이스의 각 필드는 `Field`클래스의 객체가 됨

  - CharField
    - 교재의 예제에서 문자를 저장하기위해 사용하고있음
    - 필수 파라미터로 `max_length`를 지정해줘야 함
  - [장고의 필드타입들](https://docs.djangoproject.com/en/4.0/ref/models/fields/#model-field-types)

- 모델을 정의하는 방법

  - `models.py`에 다음과 같이 클래스를 추가해 준다

- ```
  from django.db import models
  
  # Create your models here.
  # 클래스의 이름이 모델(테이블)의 이름이 됨    
  class Todo( models.Model ):
      # content 컬럼을 정의
      # 이 컬럼의 타입은 문자타입이다
      content = models.CharField(max_length=255)
  ```



### 모델을 적용

- 이렇게 만들어진 모델을 실제 DB에 반영

- 적용하는 방법

  - 모델을 변경시킨 내용과 변경사항을 장고에게 알려준다

- ```
  python manage.py makemigrations 앱이름
  ```

  - 변경사항을 실제 DB에 반영시킨다

- ```
  python manage.py migrate
  ```



## createTodo 기능 추가

- 전달받은 할 일을 디비에 저장
  - URL과 view를 연결
  - view에서는 해당 기능을 구현



### urls.py

- `createTodo`요청과 views를 연결

- /프로젝트폴더/앱폴더/urls.py

- 아래와 같이 추가 해준다

- ```
  urlpatterns = [
      path('', views.index),
  
      # createTodo에 대한 URL요청과 view를 연결해준다
      path('createTodo/', views.createTodo),
  ]
  ```



### views.py -1

- `URLconf`에서 설정된 내용대로 함수를 정의해준다

  - 연결이 잘 되었는지 확인하기 위해서 아래와 같이 추가

- /프로젝트폴더/앱폴더/views.py

- ```
  from django.http import HttpResponse
  
  def createTodo( request ):
    # URL과 view가 잘 연결되었는지 확인해보자
    return HttpResponse('createTodo를 할거야')
  ```



### views.py -2

- 입력한 값이 서버(장고)로 잘 전달되는지 확인

  - views.py의 `createTodo`함수를 아래와 같이 수정해서 확인

- ```
  def createTodo( request ):
    # URL과 view가 잘 연결되었는지 확인해보자
    # return HttpResponse('createTodo를 할거야')
  
    # 사용자가 입력한 할일을 잘 받아오는지 확인
    # 입력값 전달은 POST방식으로, 'todoContent'변수를 통해서 전달된다
    user_input_str=request.POST['todoContent']
    return HttpResponse(f'사용자가 입력한 값:{user_input_str}')
  ```

  

## 디비에 저장하기



### urls.py

- 입력을 처리하고 다시 첫 페이지로 돌아가기 위해서 아래와 같이 수정

  - index에 대해서 `name`파라미터를 추가

- /프로젝트폴더/앱폴더/urls.py

- ```
  urlpatterns = [
  	# name='index' 추가
      path('', views.index, name='index'),
  
      # createTodo에 대한 URL요청과 view를 연결해준다
      path('createTodo/', views.createTodo),
  ]
  ```



### views.py

- 전달받은 값을 디비에 저장하기위한 코드를 추가

- /프로젝트폴더/앱폴더/views.py

- ```
  from django.shortcuts import render
  from django.http import HttpResponse, HttpResponseRedirect
  
  # 미리 만들어진 model을 가져오도록 한다
  from .models import *
  
  # index 페이지로 돌아가기 위한 reverse를 임포트 한다
  from django.urls import reverse
  
  # Create your views here.
  def index( request ):
    return render(request, 'my_to_do_app/index.html')
  
  def createTodo( request ):
  
    user_input_str = request.POST['todoContent']
    # models.py에서 정의된 클래스를 이용해서 전달받은 값을 DB에 저장
    new_todo = Todo( content = user_input_str )
    new_todo.save()
  
    return HttpResponseRedirect(reverse('index'))
  ```

  

### index.html

- 책의 예제는 지금 단계에서는 동작하지 않기 때문에 수정된 `index.html`을 사용해야한다

- ```
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
  
      <!-- Boot strap -->
      <!-- 합쳐지고 최소화된 최신 CSS -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
      <!-- 부가적인 테마 -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
      <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
  
      <style>
          .content{
              height: 75%;
          }
          .messageDiv{
              margin-top: 20px;
              margin-bottom: 50px;
          }
          /*
          .toDoDiv{
  
          }
          */
          .custom-btn{
              font-size: 10px;
          }
          .panel-footer{
              height:10%;
              color:gray;
          }
      </style>
  
      <title>To-Do</title>
  </head>
  <body>
      <div class="container">
          <div class="header">
              <div class="page-header">
                  <h1>To-do List <small>with Django</small></h1>
              </div>
          </div>
          <div class="content">
              <div class="messageDiv">
                  <form action="./createTodo/" method="POST">{% csrf_token %}
                      <div class="input-group">
                          <input id="todoContent" name="todoContent" type="text" class="form-control" placeholder="메모할 내용을 적어주세요">
                          <span class="input-group-btn">
                              <button class="btn btn-default" type="submit">메모하기!</button>
                          </span>
                      </div>
                  </form>
              </div>
  
              <div class="toDoDiv">
                  <ul class="list-group">
                      {% for todo in todos %}
                      <form action="./doneTodo/" method="GET">
                          <div class="input-group" name='todo1'>
                              <li class="list-group-item">{{ todo.content }}</li>
                              <input type="hidden" id="todoNum" name="todoNum" value="{{ todo.id }}"></input>
                              <span class="input-group-addon">
                                  <button type="submit" class="custom-btn btn btn-danger">완료</button>
                              </span>
                          </div>
                      </form>
                      {% endfor %}
                  </ul>
              </div>
          </div>
          <div class="panel-footer">
              실전예제로 배우는 Django. Project1-TodoList
          </div>
      </div>
  </body>
  </html>
  ```

  



## static

- 정적 파일 관리
  - 장고에서는 정적인 파일을 관리하는 통합된 환경을 제공
  - CSS, 이미지, 등등



### static 폴더 설정

- settings.py

- ```
  STATIC_URL = 'static/'
  
  # 아래처럼 static 폴더에 대한 경로를 설정
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  ```

- BASE_DIR 은 프로젝트폴더 가 된다

  - 프로젝트폴더 에 static 폴더를 하나 만들어 준다
  - /프로젝트폴더/static

- 폴더가 생성되었으면 HTML에 필요한 CSS 파일을 해당 폴더로 복사해줌



### CSS 설정

- 템플릿 태그를 사용해서 지정된 static 폴더로부터 css 파일을 임포트 한다

- ```
   {% load static %}
   <link type='text/css' rel='stylesheet' href='{% static "bootstrap.min.css" %}' />
   <link type='text/css' rel='stylesheet' href='{% static "bootstrap-theme.min.css" %}' />
   <link type='text/css' rel='stylesheet' href='{% static "list.css" %}' />
  ```





## 모델

- 게시글을 저장하기 위한 테이블을 정의

- ```
  from django.db import models
  
  # Create your models here.
  # ORM (Object Relation Mapping)
  
  class board( models.Model ):
      createDate = models.DateField()
      writer = models.CharField(max_length=128)
      subject = models.CharField(max_length=255)
      content = models.TextField()
  ```

- 장고에서는 클래스가 곧 테이블이 된다

  - 작성된 클래스를 DB에 반영해준다

- ```
  prompt> python manage.py makemigrations 앱이름
  
  prompt> python manage.py migrate
  ```



### 모델 테스트

- prompt> python manage.py shell

- ```
  >>> from board     .      models      import        Board
          -------        -----------               ----------
          package           module                 models.py에 정의된 Board 클래스
  
  >>> import datetime
  >>> b = Board( createDate=datetime.date.today(), writer='글 작성자', subject='글 제목', content='글 내용')
  
  >>> b.save()
  ------------
  생성된 객체를 테이블에 저장
  
  >>> Board.objects.all()
  ------------------------
  테이블에 저장된 모든 row를 객체형태로 반환
  
  <QuerySet [<board: board object (1)>, <board: board object (2)>, <board: board object (3)>]>
  ------------------------------------------------------------------------
  쿼리셋 타입의 객체가 반환
  테이블 내의 각 row는 하나의 Board 객체로 매핑이 된다.
  
  >>> for b in Board.objects.all():
    print(b.subject)
  -----------------------------------------
  쿼리셋 객체는 이터레이블 객체
  
  >>> Board.objects.filter(id=1)
  ------------------------------
  쿼리셋 객체를 반환
  
  >>> Board.objects.get(id=1)
  ------------------------------
  Board 타입의 객체 하나를 반환
  ```

  





































