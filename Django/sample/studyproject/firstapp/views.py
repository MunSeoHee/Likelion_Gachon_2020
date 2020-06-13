from django.shortcuts import render
import random

def hello(request):
    return render(request, 'hello.html')

def lotto(request):
    lotto_num = random.sample(range(1,46), 6)
    return render(request, 'lotto.html', {'lotto':lotto_num})
# Create your views here.
