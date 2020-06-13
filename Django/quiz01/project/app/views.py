from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request, 'signin.html')

def show(request):
    check1=request.GET.get('check1')
    check2=request.GET.get('check2')
    if(check1=='True' and check2=='True'):
        name=request.GET['name']
        id=request.GET['email']
        pw=request.GET['pw']
        pw_check=request.GET['pw_check']
        if(pw==pw_check):
            return render(request, 'show.html', {'msg':'가입이 완료되었습니다'})
        else:
            return render(request, 'show.html', {'msg':'비밀번호가 일치하지 않습니다'})
    else:
        return render(request, 'show.html', {'msg':'약관에 동의해주세요'})
       