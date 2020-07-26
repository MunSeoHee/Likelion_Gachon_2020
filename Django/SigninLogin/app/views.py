from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    return render(request, 'home.html')

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

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/home')
    return render(request, 'home.html')