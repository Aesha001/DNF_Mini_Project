from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from PayOnline import views
from django.urls import path
 
app_name = 'donate'
urlpatterns = [
    path('',views.first ,name='first'),
    path('success/' , views.success , name='success'),
    path('home/', views.home , name='home'),
]