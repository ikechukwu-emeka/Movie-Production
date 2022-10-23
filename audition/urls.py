from django.urls import path
from.views import *

urlpatterns = [
 path('',dashboard,name='dashboard'),
    path('about',about,name='about'),
    path('services',services,name='services'),
    path('login',log_in,name='login'),
    path('sign_up',sign_up,name='sign_up'),
    path('team',team,name='team'),
    path('homepage',homepage,name='homepage'),
    path('logout',log_out,name='logout')
    
]
