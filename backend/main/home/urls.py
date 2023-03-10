from django.urls import path
from .views import Home,  Profile, Announcement , Login
from .models import LoginForm
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('',Home,name = 'home'),
    path('profile/',Profile,name= 'profile'),
    path('announcment/',Announcement,name= 'announcment'),
    path('login/',Login,name= 'login'),
    path('logout/',LogoutView.as_view(),name= 'logout'),
    
]
