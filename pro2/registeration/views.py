from django.contrib import messages
from django.contrib.messages.api import success
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

# Create your views here.

def signup(request):
    if request.method=='POST':
    
        bgroup=request.POST['bgroup']
        phone=request.POST['phone']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        

        if password==password1:
            if User.objects.filter(username=username).exists():
                return JsonResponse(
                    {'success':False,'nameerror':True},
                    safe=False
                )
                 
            elif User.objects.filter(email=email).exists():
                return JsonResponse(
                    {'success':False , 'emailerror':True},
                    safe=False
                )

            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                table_bgroup.objects.create(bgroup=bgroup,phone=phone,user=user)
                
                print('user created')
                return JsonResponse(
                    {'success':True},
                    safe=False
                )

        else:
            print("password not matching")
            return JsonResponse(
                    {'success':False,'passerror':True},
                    safe=False
                )
    else:
        return render(request,'signup.html')


def login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect(display)
        else:
            messages.info(request,'invalid credentials')
            return redirect(login)
            
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)  
    return redirect('/')
    
def display(request):
    
    users=User.objects.all()
    
    for user in users:
       temps=table_bgroup.objects.filter(user=user).first()
       user.bgroup=temps.bgroup
       user.phone=temps.phone
        
    return render(request,'display.html',{'users':users})

def add(request):
    return render(request,'signup.html')
