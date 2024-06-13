from django.shortcuts import render, HttpResponse

def index(request):
    # student = {
    #     'values':[32,43,54,65,12,43,90,44,32,21]
    # }
    # student = {
    # "Sno": [1,2,3,4,5],
    # "name": ["Ranjith", "Niranjan", "sagar", "alfa", "beta"],
    # "physics": [80,70,60,50,45],
    # "chemistry": [75,40,80,50,67],
    # "maths": [70,75,60,83]
    # }
    return render(request,'index.html')
