from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import  login , logout , authenticate



def Home(request):
    return render(request,'home/base.html',context={'title':'Home'})


    
@login_required
def Announcement(request):
    return render(request,'home/announcment.html',context={'title':'Announcment'})


def Profile(request):
    return render(request,'home/profile.html',context={'title':'Profile'})