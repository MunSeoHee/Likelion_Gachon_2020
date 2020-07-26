from django.shortcuts import render, get_object_or_404, redirect
from .models import list
# Create your views here.
def index(request):
    ob = list.objects
    return render(request, 'index.html', {'ob':ob})

def detail(request, id):
    ob = get_object_or_404(list,pk=id)
    return render(request, 'detail.html', {'ob':ob})

def delete(request, pk_id):
    ob = get_object_or_404(list,pk=pk_id)
    ob.delete()
    return redirect('/')

def update(request, pk_id):
    ob = get_object_or_404(list,pk=pk_id)
    return render(request, 'update.html', {'ob':ob})

def updat(request, pk_id):
    ob = get_object_or_404(list,pk=pk_id)
    ob.title = request.GET['title']
    ob.text = request.GET['text']
    ob.save()
    return redirect('/'+str(pk_id))