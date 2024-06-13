from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def laptops(request):
    return render(request, 'laptops.html')

def mobiles(request):
    return render(request, 'mobiles.html')

def check_db_connection(request):
    try:
        # connection.ensure_connection()
        check = connection.ensure_connection()
        print("Check status:", check)
        return HttpResponse("Connection to MySQL is successful")
    except Exception as e:
        return HttpResponse(f"Connection failed: {e}")
    


# def Home(request):
#     return HttpResponse("Hello Student How are you doing ")