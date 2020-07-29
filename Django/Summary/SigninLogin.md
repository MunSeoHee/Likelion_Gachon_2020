## Signin Login

### Signin Login

#### 01. Login Signin URL 작성
```
    path('signup',app.views.signup, name='signup'),
    path('login', app.views.login, name='login'),
```

#### 02. Login Templates 작성
```{% csrf_token %}``` : Django에서 보안을 위해 제공해주는 기능
```html
{% if error %}
{{ error }}
<br>
<br>
{% endif %}
<h1>Login</h1>
<form method="POST" action="{% url 'login'%}">
    {% csrf_token %}
    Username:
    <br>
    <input name="username" type="text" value="">
    <br>
    Password:
    <br>
    <input name="password" type="password" value="">
    <br>
    <br>
    <input class="btn btn-primary" type="submit" value="Login">
</form>
```


#### 03. Signin Templates 작성
```html
{% if error %}
{{ error }}
<br>
<br>
{% endif %}

<h1>Sign Up!</h1>

<form method="POST" action="{% url 'signin'%}">
    {% csrf_token %}
    Username:
    <br>
    <input name="username" type="text" value="">
    <br>
    Password:   
    <br>
    <input name="password1" type="password" value="">
    <br>
    Confirm Password:
    <br>
    <input name="password2" type="password" value="">
    <br>
    <br>
    <input class="btn btn-primary" type="submit" value="Sign Up!">
</form>
```


#### 04. Signin view 작성

```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': '비밀번호와 비밀번호 확인이 일치하지 않습니다'})
    return render(request, 'signin.html')

```
```user = User.objects.create_user(username, password)``` : User 클래스를 기반으로 유저를 만드는 함수

```auth.login``` : 로그인 시켜주는 함수


#### 05. Login view 작성
```python
@csrf_exempt
def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/home')
            else:
                return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
```
```user = auth.authenticate(request, username=username, password=password)``` : username과 password로 사용자가 존재하는지 판단, 사용자 존재할경우 로그인

---------

### Logout Login정보


#### 01. Logout View 작성
``` python
@csrf_exempt
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/home')
    return render(request, 'home.html')
```


#### 02. Logout url 추가
```python
path('logout', app.views.logout, name='logout'),
```

#### 03. 로그인 시 logout 버튼 및 로그인 정보 보여주기
```html
{% if user.is_authenticated %}
환영합니다. {{ user.username }} 님!
<form id="logout" method="POST" action="{% url 'logout' %}">
    {% csrf_token %} <input type="submit" value="로그아웃"/>
</form> 
```

#### 04. Login 되어 있지 않을 경우 처리
```html
{% else %}                   
<a href="{% url 'signin' %}">Signup</a>
<a href="{% url 'login' %}">Login</a>
{% endif %}
```

#### 05. 위의 페이지 보여 줄 url, view 작성
```python
path('home', app.views.home, name='home')
```
```python
def home(request):
    return render(request, 'home.html')
```