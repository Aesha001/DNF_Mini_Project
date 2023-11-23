from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [

    path("", views.core,name='home'),
    path("aboutus/", views.aboutus,name='aboutus'),
    # path("contactus/", views.contactus,name='contactus'),
    path("blog/", views.blog,name='blog'),
    path("search/", views.search,name='search'),
    path("profile/", views.profile,name='profile'),

]