from django.contrib import admin

from PayOnline.models import Pay

# Register your models here.
from .models import Pay
admin.site.register(Pay)