from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
import datetime

# Create your views here.
def index(request):
    blogs = Blog.objects
    return render(request, 'index.html', {'blogs':blogs})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.contents = request.GET['contents']
    blog.save()
    return redirect('/')

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

def delete(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.delete()
    return redirect('/')

def update(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'update.html', {'blog':blog})

def renew(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.title = request.GET['title']
    blog.contents = request.GET['contents']
    blog.date = datetime.datetime.now()
    blog.save()
    return redirect('/'+str(id))

def blog(request):
    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog.html', {'posts':posts})