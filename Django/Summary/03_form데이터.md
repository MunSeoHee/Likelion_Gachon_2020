## 03 _ form 데이터 처리

### 입력 페이지 만들기

#### 01. App 생성
```
python manage.py startapp firstapp
```

#### 02. settings.py에 App 추가
```
INSTALLED_APPS = [
    'Firstapp.apps.FirstappConfig'
]
```

#### 03. templates 폴더에 화면 생성
Firstapp/templates/index.html
```
<h1>이름을 입력해주세요</h1>

<form action="{% url 'name' %}" method="GET">
    <input type="text" name="name">
</form>
```


#### 04. index.html을 보여주기 위한 함수 생성
Firstapp/views.py
```
def index(request):
    return render(request, 'index.html')
```


#### 05. url 설계
```
import firstapp.views

urlpatterns = [
    path('/', firstapp.views.index, name="home")
]
```

---------

### 결과 페이지 만들기

#### 01. 03. templates 폴더에 결과 화면 생성
Firstapp/templates/name.html
```
<h1>당신의 이름은</h1>
<p>{{name}}</p>
```
템플릿 언어를 이용하며 name이라는 변수의 값을 화면에 뿌린다<br>

#### 02. name.html을 보여주기 위한 함수 생성
Firstapp/views.py
```
def name(request):
    name = request.GET['name']
    return render(request, 'name.html', {'name':name})
```
```GET```방식으로 넘어오는 이름이 ```'name'인 input의 value```를 ```name```이라는 변수에 저장<br>
Key:Value의 형식으로 'name'이라는 이름으로 ```'name'변수를 name.html```에 전송한다

#### 03. url 설계
```
import firstapp.views

urlpatterns = [
    path('/', firstapp.views.index, name="home"),
    path('/name', firstapp.views.name, name="name")
]
```