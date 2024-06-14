from django.shortcuts import render, HttpResponse
from .forms import student

def index(request):
    context={}
    context['form'] = student()
    return render(request,'index.html',context)

def fruits(request):
    items = {'Apple': 3, 'Banana': 2, 'Cherry': 5, 'Date': 7}
    return render(request, 'fruits.html', {'items': items})