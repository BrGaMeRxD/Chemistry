from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView 
# Create your models here.

class User_db(User):
    code_meli = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
    
class LoginForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder':'شماره موبایل','class':'login-panel-forms'}))
    
    class Meta():
        model = User_db
        fields = ['phone_number']
