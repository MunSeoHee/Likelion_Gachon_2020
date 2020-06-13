from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    text=request.GET['text']
    count = len(text)
    return render(request, 'word.html', {'text':count})

def blog(request):
    blog = Blog.objects
    return render(request,'blog.html', {'blogs':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['text']
    blog.body = request.GET['body']
    blog.like = request.GET['like']
    blog.save()

    return redirect('/blog')

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})

def delete(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/blog')

def update(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'blog':blog})

def ud(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['text']
    blog.body = request.GET['body']
    blog.like = request.GET['like']
    blog.date = datetime.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog_id))