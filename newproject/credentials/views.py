from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from zmq.backend.cython import message


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username =request.POST['username']
        password =request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Try another Username")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
                user.save();
                print("User Created")
        else:
            messages.info(request,"Passwords not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

