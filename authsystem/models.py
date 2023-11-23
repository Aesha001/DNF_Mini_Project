from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
# Create your models here.


gender_choice = (

    ('male','Male'),
    ('female','Female')
)

class CustomUser(AbstractUser):
    gender_choice = models.CharField(max_length=20, choices=gender_choice,default='male')
    contact = models.CharField(max_length=10, default='') 
    area_name = models.CharField(max_length=200,blank=True,null=True)
    pin_code = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(default='name@email.com', blank=True, null=True)


    # Specify unique related_name attributes to avoid clashes
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')
