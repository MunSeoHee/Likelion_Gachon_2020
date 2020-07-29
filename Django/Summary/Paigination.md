## Paigination

### Paigination
Blog Model을 만들어 두었다는 가정 하에 진행

#### 01. paigination을 위한 view 작성
```python
from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

def index(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html',{'blogs':blogs,'posts':posts})
```

#### 02. paigination 된 데이터를 표시 할 html 작성
```html
{% for blog in posts %}

    <a href="{%url 'detail' blog.id%}" >{{blog.title}}</a><br>

{%endfor%}
```


#### 03. 다음 페이지, 이전 페이지 버튼 만들기
```html
{%if posts.has_previous%}
<a href="?page=1">First</a>
<a href="?page={{posts.previous_page_number}}">Previous</a>
{%endif%}

<span>{{posts.number}}</span>
<span>of</span>
<span>{{posts.paginator.num_pages}}</span>

{%if posts.has_next%}
<a href="?page={{posts.next_page_number}}">Next</a>
<a href="?page={{posts.paginator.num_pages}}">Last</a>
{%endif%}
```
