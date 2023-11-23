from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path("", views.product,name='product'),
    path("category/<slug:val>", views.category,name='category'),
    path("productdetail/<int:id>", views.productdetail,name='productdetail'),
    path("test/", views.test,name='test'),
    path("carttest/", views.carttest,name='carttest'),

    path("add_to_cart/<int:prod_id>/", views.add_to_cart,name='add_to_cart'),
    path("showcart/", views.showcart,name='showcart'),
    path('product/order_create/', views.order_create, name='order_create'),
    # path('order_create_no_id/<int:prod_id>', views.order_create, name='order_create_no_id'),

    # path('product/order_create/', views.order_create, name='order_create_no_id'),
  
    path('wishlist/<int:product_id>/',views.wishlist_add,name='wishlist'),
    path('wishlist/',views.wishlist_show,name='wishlist_show'),
    path("<int:product_id>/delete/",views.delete_item,name='delete_item'),
    
    path('contactus/', views.contactus, name='contactus'),
    path("payment/",views.payment,name='payment'),

    # path("checkout/",views.checkout,name='checkout')
    
]