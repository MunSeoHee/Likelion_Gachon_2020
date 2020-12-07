from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error': '로그인 에러'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'error':'비번 비번확인 불일치'})
    return render(request, 'signup.html')

def index(request):
    return render(request, 'index.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('/')