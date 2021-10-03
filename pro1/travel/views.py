from django.shortcuts import render
from .models import Destinaton
# Create your views here.
def index(request):
    dests=Destinaton.objects.all()

    
    return render(request,'index.html',{'dests':dests})
