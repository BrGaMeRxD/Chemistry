from django.shortcuts import render,redirect
from .models import LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import  login , logout , authenticate
from .models import LoginForm

# Create your views here.

def Home(request):
    return render(request,'home/base.html',context={'title':'Home'})
def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.method)
        if form.is_valid():
            print('hahahha')
    else:
        form = LoginForm()
    return render(request,'home/login.html',context = {'title':'Login','form':form})

    
@login_required
def Announcement(request):
    return render(request,'home/announcment.html',context={'title':'Announcment'})


def Profile(request):
    return render(request,'home/profile.html',context={'title':'Profile'})