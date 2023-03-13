from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils import timezone
# Create your models here.

class Student(AbstractUser):
    clasha = [('DAHOM','دهم'),('YAZDAHOM','یازدهم'),('DAVAZDAHOM','دوازدهم'),('FAREGHOLTAHSIH','فارغ التحصیل')]
    username = models.CharField(max_length=16,unique=True)
    clasa = models.CharField(max_length=16,choices=clasha,default='NOT_SET')
    code_meli = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10,default='')
    date_created  = models.TimeField(default=timezone.now)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['username','password','phone_number']
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ('phone_number',)
    objects = CustomUserManager()
    
    
    def __str__(self):
        return self.username
    
    

