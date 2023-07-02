from django.db import models
from django.db import models
from .models import*
 
class Message(models.Model):
     firstname=models.CharField(max_length=50,null=True)
     email_id=models.CharField(max_length=50,null=True)
     phoneno=models.CharField(max_length=50,null=True)
     packages=models.CharField(max_length=50,null=True)
     Date=models.CharField(max_length=50,null=True)
     Messages=models.CharField(max_length=50,null=True)
# Create your models here.
