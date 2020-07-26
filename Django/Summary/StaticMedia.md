## Static Media

### Staitc file
개발하는 단계에서 생성되는 쓰임이 정해져있는 파일들 (css, js, image 파일 등)

#### 01. Static 폴더 생성
app 폴더 안에 ```static``` 이라는 이름의 폴더 생성

#### 02. settings.py에 Static 폴더 인식 시키기
settings.py 파일 맨 밑에 다음과 같은 코드 추가
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app폴더', 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```


#### 03. static 파일들을 한 곳에 모으기
app폴더/static폴더 안에 필요한 파일들을 담고 콘솔에 다음과 같은 명령어 입력
```
python manage.py collectstatic
```


#### 04. Static  파일 사용하기
static 파일을 사용하고자 하는 template에 다음과 같은 코드 추가
```
{% load static %}
```
static 로드 후 원하는 static 파일을 다음과 같이 사용
```
<img src="{% static 'img.jpg' %}" alt="">
```

---------

### Media file
사용자가 업로드하는 파일로 개발하는 단계에서 관리할 수 없는 파일들이기 때문에 따로 분류하여 관리

#### 01. Settings.py에 Media 설정
```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```


#### 02. Media file URL 설계
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path...
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

#### 03. Model 설계 및 생성
```
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
```
```
pip install Pillow
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
그 이후에는 기존 Model 데이터 사용과 동일하게 사용하면 됨