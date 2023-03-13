from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.views import LoginView 
import re
from django.core.exceptions import ValidationError
from home.models import Student

# Create your models here.

class RegisterForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':"form-field", 'type':"text" ,'placeholder':"اینجا وارد کنید", 'id':"reg_pass_confirm"
                           ,'maxlength':"10" ,'onkeypress':'validate(event)'}))
    username = forms.CharField(max_length=16,widget=forms.TextInput(attrs={'class':"form-field" ,'type':"text", 'placeholder':"اینجا وارد کنید", 'id':"reg_username"}))

    password1 = forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'class':"form-field" ,'type':"password" ,'placeholder':"اینجا وارد کنید", 'id':"reg_pass"
                           ,'pattern':".{5,}"}))
    password2 = forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'class':"form-field" ,'type':"password" ,'placeholder':"اینجا وارد کنید", 'id':"reg_pass"
                           ,'pattern':".{5,}"}))

    class Meta():
        model = Student
        fields = ['username','password','phone_number']

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=16,widget=forms.TextInput(attrs={'class':"form-field", 'type':"text" ,'placeholder':"اینجا وارد کنید" ,'id':"login_username"}))
    password = forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'class':"form-field", 'type':"text" ,'placeholder':"اینجا وارد کنید" ,'id':"login_pass"}))    
    
    class Meta():
        model = Student
        fields = ['username','password']
