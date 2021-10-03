from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class table_bgroup(models.Model):
    phone = models.CharField(max_length=15)
    bgroup = models.CharField(max_length=5)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    


   


    
        
