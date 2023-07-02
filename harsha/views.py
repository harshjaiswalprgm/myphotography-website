from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def index(request): 
    return render(request,"index.html")

def gallry(request): 
    return render(request,"gallery.html")

def booking(request): 
    if request.method=="POST":
        fna=request.POST["fname"]
        mail=request.POST['mailid']
        phoneno=request.POST['phno']
        package=request.POST['package']
        date=request.POST['date']
        message=request.POST['message']
        Message.objects.create(firstname=fna, email_id=mail,phoneno=phoneno,packages=package,Date=date,Messages=message)
    return render(request,"book.html")
def packge(request): 
    return render(request,"package.html")

def adminr(request): 
   data=Message.objects.all()
   oj2={"data":data}
   return render(request,"admin.html",oj2)