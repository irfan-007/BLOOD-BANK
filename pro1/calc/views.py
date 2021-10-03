from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'kukku'})

def login(request):
    val1=request.POST['user']
    val2=request.POST['password']
    return render(request,'result.html',{'result':'succecfully joined'})

