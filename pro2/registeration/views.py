from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

# Create your views here.

def signup(request):
    if request.method=='POST':
    
        bgroup=request.POST['bgroup']
        phone=request.POST['phone']

        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect(signup)

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect(signup)

            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                table_bgroup.objects.create(bgroup=bgroup,phone=phone,user=user)
                
                print('user created')
                return redirect(login)

        else:
            print("password not matching")
            messages.info(request,'password not matching')
            return redirect(signup)
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
