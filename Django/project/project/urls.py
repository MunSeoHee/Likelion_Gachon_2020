"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app01.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app01.views.index, name='index'),
    path('word',app01.views.word, name='word'),
    path('blog',app01.views.blog, name='blog'),
    path('new',app01.views.new, name='new'),
    path('create', app01.views.create, name='create'),
    path('detail/<int:blog_id>', app01.views.detail, name='detail'),
    path('delete/<int:blog_id>', app01.views.delete, name='delete'),
    path('update/<int:blog_id>', app01.views.update, name="update"),
    path('ud/<int:blog_id>', app01.views.ud, name="ud")
]
