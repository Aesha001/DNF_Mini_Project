from django.db import models
from authsystem.models import CustomUser


# Create your models here.

CATAGORY_CHOICES = (
    ('M','Mens'),
    ('W','Womens'),
    ('A','All')
)


class ProductItem(models.Model):
    
    P_name = models.CharField(max_length=100)
    P_Qty = models.IntegerField()
    P_Price = models.FloatField(max_length=15)
    CATAGORY_CHOICES = models.CharField(max_length=1, choices=CATAGORY_CHOICES, default='A')
    P_Image = models.ImageField(upload_to='image', blank=True, null=True)
    # R1_Image = models.ImageField(upload_to='image', blank=True, null=True)
    # R2_Image = models.ImageField(upload_to='image', blank=True, null=True)
    P_Desc = models.CharField(max_length=1000)
    # P_Discount = models.FloatField(max_length=15)
    #customer_id = models.ForeignKey('Customer',on_delete=models.CASCADE)
    
    def get_image_url(self):
        return f"{self.P_Image.url}"
    
    def get_image_url(self):
        return f"{self.R1_Image.url}"
    
    def get_image_url(self):
        return f"{self.R2_Image.url}"
    
    def __str__(self):
        return f"{self.P_name}"
    


    
# class Cart(models.Model):
#     user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='cartitems')
#     product_id = models.ForeignKey(ProductItem,on_delete=models.CASCADE, related_name="product_cart", null=True, blank=True)
#     quantity = models.IntegerField(default=1)

#     # def __str__(self):
#     #     return   f"{self.price} {self.Qty}" 

#     @property
#     def total_cost(self):
#         return self.quantity * self.product_id.P_Price
    
# Update your Cart model to include a ForeignKey to CustomUser
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cartitems')
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name="product_cart", null=True, blank=True)
    quantity = models.IntegerField(default=1)

    @property
    def total_cost(self):
        if self.product is not None:
            return self.quantity * self.product.P_Price
        return 0
    
class Order(models.Model):
    Full_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(ProductItem, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
# class Order(models.Model):  # order 
#     Full_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=250)
#     city = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)
    
#     class Meta:
#         ordering = ('-created',)

#     def __str__(self):
#         return f'Order {self.id}'

#     def get_total_cost(self):
#         return sum(meal.get_cost() for meal in self.meals.all())


# class OrderItem(models.Model): # ordered item
#     order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
#     item = models.ForeignKey(ProductItem,related_name='order_items',on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return str(self.id)

#     def get_cost(self):
#         return self.price * self.quantity

class WishListProduct(models.Model):
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductItem, on_delete=models.CASCADE)

class Contact_page(models.Model):
    your_name = models.CharField(max_length=150)
    Email = models.EmailField()
    subject = models.CharField(max_length=150)
    text = models.TextField(max_length=500)
    
    def __str__(self):
        return f"{self.your_name}"
