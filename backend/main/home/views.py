from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'home/home.html',context={'title':'Home'})

def Contact(request):
    return render(request,'home/contact.html',context={'title':'Contact'})