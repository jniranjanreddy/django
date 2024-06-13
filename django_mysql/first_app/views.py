from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return render(request, 'index.html', {'name': 'John', 'age': 30}) # This line returns the index.html template

def Home(request):
    return HttpResponse("Hello Student How are you doing ")

def sagar(request):
    return HttpResponse("Hello Sagar How Are you doing ")


def niky(request):
    return HttpResponse("<h1>I am a Disco dancer </h1>")