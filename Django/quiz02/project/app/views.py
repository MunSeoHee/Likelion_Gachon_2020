from django.shortcuts import render
from .models import User
def user(request):
    user = User.objects
    return render(request, 'user.html', {'users':user})

# Create your views here.
