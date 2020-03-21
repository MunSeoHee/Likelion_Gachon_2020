## 02 _ Django 프로젝트 시작하기

### Django 프로젝트

#### 프로젝트 기본 파일 및 폴더
```
manage.py
프로젝트폴더
    __pycache__
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
```

#### Django 프로젝트 폴더 및 파일 역할
```settings.py```
<br>현재 Django 프로젝트의 환경 및 구성을 저장하는 파일
<br><br>
```urls.py```
<br> 어떤 url 요청이 들어왔을 때 무엇이 보여지게 할 것인지 설정하는 파일

-------

### APP

#### App 생성하기
```
python manage.py startapp app이름
```


#### App 폴더 구조
```
App 폴더
    migration 폴더
    __init.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

#### App 폴더 및 파일 역할
```views.py```
<br> 어떠한 요청이 들어왔을 때, 어떤 동작을 하고 어떤 화면을 보여줄 것인지에 대한 함수를 작성
<br><br>
```urls.py```
<br>작성한 화면이 어떤 url 요청이 들어왔을 때 보여지게 할 것인지 설정

#### settings.py에 App 추가
```
INSTALLED_APPS = [
    '앱이름.apps.앱이름Config'
]

앱이름폴더 -> apps.py 파일 안에 적힌 class '앱이름Config'를 의미
```
Django 프로젝트는 App이 생성된 것을 인식하지 못하고 있다. 따라서 다음과 같은 절차를 통해 App이 생성 되었음을 인지하도록 설정해준다.


#### templates 폴더 생성
```
App이름 폴더 안에 templates 폴더를 하나 생성
그 안에 사용자에게 보여질 화면(html)을 작성
```

#### 요청 처리 할 함수 정의
App 폴더의 ```views.py``` 파일
```
def index(request):
    return render(request, 'index.html')
```
index() 함수가 실행 될 경우, index.html을 사용자에게 보여주게 된다.
#### url 설계
```urls.py```
1. app폴더의 views.py를 urls.py에 import
```
import firstapp.views
```
2. url 경로 추가
```
urlpatterns = [
    path('/', 앱폴더.views.index, name="home")
]
```
```''```라는 url요청이 들어오면 앱폴더의 ```views.py``` 파일의 ```index()```함수를 실행하게 된다. 그리고 이러한 작업의 이름을 home으로 설정하게 된다.<br><br>
**path(url요청, 호출 할 함수, 해당 패턴의 이름)**
