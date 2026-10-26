from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

def home(request):
    context={
        'name':"Dheeraj",
        'age':20,
        'branch':'Computer Science & Engineering'
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')
