from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import  login , logout , authenticate
from .models import LoginForm,RegisterForm
from authenticate.models import Student
from django.contrib.auth.hashers import make_password
import re
# Create your views here.

def Login(request):
    error_list = {}
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        if 'phone_number' in request.POST:
            def clean(username,pass1,pass2,phone_number):
                error_list = {}
                if pass1 != pass2:
                    error_list['password'] = True
                try:
                    user = Student.objects.get(username=username)
                    error_list['username'] =  True
                except:
                    pass
                if re.search(r'(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}',phone_number) == None:
                    error_list['phone_number'] = True
                return error_list
            register_form = RegisterForm(request.POST)
            print(request.POST)
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            pn = request.POST['phone_number']
            error_list = clean(username,password1,password2,pn)
            if not clean(username,password1,password2,pn):
                user = Student.objects.create_user(username = username,password=password1,phone_number= pn)
        else:
            login_form  = LoginForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = Student.objects.get(username=username)
            except:
                error_list = {'username':True}
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request=request,user=user)
                print('logged-in')
                return redirect('home')
                
    register_form = RegisterForm()
    login_form = LoginForm()
    print(error_list)
    return render(request,'authenticate/login.html',context = {'title':'Login','rform':register_form,'lform':login_form,'errors':error_list})

@login_required
def Logout(request):
    if request.user.is_authenticated:
        logout(request=request)
        return redirect('login')
    