from webscrap.settings import AUTH_PASSWORD_VALIDATORS
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name =request.POST['last_name']
        email =request.POST['email']
        password = request.POST['password']

        x= User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        x.save()
        print("user created")
        return redirect('/')


    else:    
        return render(request,'signup.html')


def login(request):
    if request.method=='POST':
       username1=request.POST['username']
       password1=request.POST['password']
       from django.contrib import auth
       x=auth.authenticate(username=username1,password=password1)
       if x is None:
           return redirect('login')
       else:
           return redirect('/')    
    else:
         return render(request,'login.html')        