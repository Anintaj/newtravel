from django.http import HttpResponse
from django.shortcuts import render
from .models import newdb
from . models import team

# Create your views here.
def home(request):
    obj=newdb.objects.all()
    abc=team.objects.all()

    #return HttpResponse("This is Your Home Page")
    return render (request,"index.html",{'a':obj,'b':abc})
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("This is Your Contact Page")
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    result=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return render(request,"Details.html",{'res':result,'s':sub,'m':mul,'d':div})
def thanks(request):
    return render(request,"Thanks.html")

