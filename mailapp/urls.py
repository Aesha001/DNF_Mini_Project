from unicodedata import name
from django.urls import path
from .import views

app_name = 'mailapp'
urlpatterns = [
    path('mail/', views.mail_function, name='mail'),
    path('thanks/', views.thanks_function, name="thanks"),
]
