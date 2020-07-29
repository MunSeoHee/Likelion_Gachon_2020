from django.shortcuts import render, redirect, get_object_or_404
from .models import Lol
# Create your views here.
def index(request):
    x = Lol.objects
    return render(request, 'index.html', {'x':x})

def create(request):
    return render(request, 'create.html')

def new(request):
    #모델 새 오브젝트 -> 각 필드 값 채워넣기 -> 저장
    x = Lol()
    x.name = request.GET['name']
    x.gender = request.GET['gender']
    x.hp = request.GET['hp']
    x.text = request.GET['text']
    x.save()
    return redirect('/')

def detail(request, id):
    x = get_object_or_404(Lol, pk = id)
    return render(request, 'detail.html', {'x':x})

def delete(request, id):
    x = get_object_or_404(Lol, pk = id)
    x.delete()
    return redirect('/')

def update(request, id):
    x = get_object_or_404(Lol, pk = id)
    return render(request, 'update.html', {'x':x})

def renew(request, id):
    x = get_object_or_404(Lol, pk = id)
    x.name = request.GET['name']
    x.gender = request.GET['gender']
    x.hp = request.GET['hp']
    x.text = request.GET['text']
    x.save()
    return redirect('/'+str(id))
    