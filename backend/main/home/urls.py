from django.urls import path
from .views import Home , Contact

urlpatterns = [
    path('',Home,name = 'home'),
    path('contact/',Contact,name= 'contact')
    
    
    
]