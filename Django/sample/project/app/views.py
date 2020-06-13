from django.shortcuts import render
from .models import Blog

def blog(request):
    blog = Blog.objects
    return render(request,'blog.html', {'blogs':blog})

def index(request):
    return render(request, 'index.html')

def word(request):
    word = request.GET['text']
    count = len(word)
    return render(request, 'word.html', {'count':count})

def input(request):
    return render(request, 'input.html')

def hello(request):
    name = request.GET['name']
    age = request.GET['age']
    return render(request, 'hello.html', {'name':name, 'age':age})


# Create your views here.
