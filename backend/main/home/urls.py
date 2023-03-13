from django.urls import path
from .views import Home,  Profile, Announcement
urlpatterns = [
    
    path('',Home,name = 'home'),
    path('profile/',Profile,name= 'profile'),
    path('announcment/',Announcement,name= 'announcment'),
    
]
