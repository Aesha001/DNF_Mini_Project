from django.contrib import admin

# Register your models here.
from .models import ProductItem,Cart,Order,OrderItem
admin.site.register(ProductItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)