from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from product.models import ProductItem, Cart, Order, OrderItem, WishListProduct
from .forms import CartUpdateForm, CartRemoveForm, CartUpdateFormSet, OrderCreateForm
from authsystem.models import CustomUser
from django.http import HttpResponse
from smtplib import SMTPException, SMTPAuthenticationError
from mailapp.forms import MailForm
from mailapp.views import mail_function,send_mail
from decimal import Decimal

from django.conf import settings


# Create your views here.
def product(request):
    
    log_user = CustomUser.objects.get(pk = request.user.id)
    product = ProductItem.objects.all()
    context = {
        'product': product,
         'detail': log_user,
   
    }
    return render(request, 'product/product.html',context)


def category(request, val):
 
    log_user = CustomUser.objects.get(pk = request.user.id)
    product = ProductItem.objects.filter(CATAGORY_CHOICES=val)
    title = ProductItem.objects.filter(CATAGORY_CHOICES=val).values('P_name')
    context = {
        'val': val,
        'product': product,
        'title': title,
        'detail': log_user,
    }
    return render(request, 'product/category.html', context)

def productdetail(request, id):
    log_user = CustomUser.objects.get(pk = request.user.id)
    pro = ProductItem.objects.get(pk=id)
    context = {
        'pro': pro,
        'detail': log_user,
    }

    return render(request, 'product/productdetail.html',context)

def test(request):
   return render(request, 'product/test.html')

def carttest(request):
   return render(request, 'product/carttest.html')




# def add_to_cart(request, prod_id):
#     user = request.user
#     product = get_object_or_404(ProductItem, id=prod_id)
#     Cart(user_id=user, product_id=product).save()
#     return redirect('product:showcart')

def add_to_cart(request, prod_id):
    user = request.user
    product = get_object_or_404(ProductItem, id=prod_id)

    # Check if the product is already in the cart
    if Cart.objects.filter(user=user, product=product).exists():
        messages.warning(request, 'This item is already in your cart.')
    else:
        # Assuming 'user' is a CustomUser instance with a numeric 'id' field
        cart_item = Cart(user=user, product=product)
        cart_item.save()
        messages.success(request, 'Item added to your cart successfully.')

    return redirect('product:showcart')


# def showcart(request):  final
#     user_id = request.user.id
#     cart = Cart.objects.filter(user_id=user_id)

#     total = 0
#     for item in cart:
#         total += item.total_cost
    
#     context = {
#         'cart': cart,
#         'total': total
#     }
#     return render(request, 'product/addtocart.html', context)

def showcart(request):
    log_user = CustomUser.objects.get(pk = request.user.id)
    user = request.user
    cart_items = Cart.objects.filter(user_id=user)
    total = sum(item.total_cost for item in cart_items)

    if request.method == 'POST':
        if 'update_quantity' in request.POST:
            cart_item_id = request.POST.get('update_quantity')
            new_quantity = request.POST.get(f'quantity_{cart_item_id}')
            cart_item = Cart.objects.get(id=cart_item_id)
            cart_item.quantity = new_quantity
            cart_item.save()
            messages.success(request, 'Quantity updated successfully.')

        elif 'remove_item' in request.POST:
            cart_item_id = request.POST.get('remove_item')
            Cart.objects.filter(id=cart_item_id).delete()
            messages.success(request, 'Product removed from cart.')

        return redirect('product:showcart')

    return render(request, 'product/addtocart.html', {'cart_items': cart_items, 'detail': log_user,'total': total,'messages': messages.get_messages(request)})


# def add_to_cart(request,prod_id):
#     user_id = request.user.id
#     product_id = request.GET.get('prod_id')
#     product = ProductItem.objects.get(id=prod_id)
#     Cart(user_id=user_id, product_id=product).save()
#     return redirect('product:showcart')

# def showcart(request):
#     user_id = request.user_id
#     cart = Cart.objects.filter(user_id=user_id)
#     return render(request, 'product/addtocart.html', {'cart':cart})



#---------------------------------------------------------------------
def payment(request):
    return render(request, 'Payment/checkout.html')



def order_create(request):
    # Fetch the cart items
    log_user = CustomUser.objects.get(pk = request.user.id)
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    total = Decimal(sum(item.total_cost for item in cart_items))

    discount = Decimal('0.1') * total
    # discount = discount_percentage * Decimal(total)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()


            # Iterate over items in the cart and create OrderItem instances
            for cart_item in cart_items:
                product = cart_item.product
                order_item = order.items.create(
                item=product,
                price=product.P_Price,
                quantity=cart_item.quantity
                  )
                order_item.save()

            # Clear the cart after creating order items
            cart_items.delete()

            # Redirect to a success page or any other desired page
            return redirect('donate:home')
    else:
        form = OrderCreateForm()

    discounted_total = total - discount

    return render(request, 'product/checkout.html', {'form': form, 'cart_items': cart_items,'total': total,'detail': log_user, 'discount': discount, 'discounted_total': discounted_total})

# def order_create(request):
#         cart = add_to_cart(request)
#         if request.method == 'POST':
#             form = OrderCreateForm(request.POST)
#             if form.is_valid():
#                 order = form.save()
#                 for product in cart:
#                     order_item = OrderItem.objects.create(order=order,
#                                              item=product['product'],
#                                              price=product['price'],
#                                              quantity=product['qty'])
#                     # clear  the cart(table)
#                     order_item.save()
#                     cart.clear()
#                     return redirect('donate:home')
#                     # return render(request, 'core/temp2.html',
#                     #               {'order': order, 'items': order.items.all()})
#         else:
#             form = OrderCreateForm()
#             return render(request,
#                       'product/checkout.html',
#                       { 'form': form})



# def contactus(request):
#     form = MailForm()
    
#     if request.method == 'POST':
#         form = MailForm(request.POST)
        
#         if form.is_valid():
#             to_mail = form.cleaned_data.get('email_id')
#             subject = form.cleaned_data.get('subject')
#             message = form.cleaned_data.get('message')
#             form.save()
            
#             #reply as email to contected person
#             try:
#                 msg = 'Your Query is recevied'
#                 send_mail(msg,
#                         'Thank you for your response....',#message
#                         settings.EMAIL_HOST_USER,
#                         [to_mail],
#                         fail_silently= False
#                         )
#             except ConnectionError as e: 
#                 print('There is an Authentication Error',e)
#             except SMTPException as e :
#                 print('There was error in sending email:  ' , e)
#             except SMTPAuthenticationError  as e:
#                 print('SMTPAuthenticationError.')
#             except socket.gaierror as r :
#                 print('There was some error in sending mail: ',r)
            
            
            
#             try:
#                 send_mail(subject,
#                         f'from: {to_mail} {message}',#message
#                         settings.EMAIL_HOST_USER,
#                         [settings.EMAIL_HOST_USER],
#                         fail_silently= False
#                         )
#             except SMTPException as e :
#                 print('There was error in sending error:  ' , e)
            
                

#             messages.warning(request,'We will reach you soon')
#             return redirect('product:contactus')
            
#     context ={
#         'form':form
#     }
#     return render(request,'core/contactus.html',context=context)


def contactus(request):
    log_user = CustomUser.objects.get(pk = request.user.id)
    form = MailForm()

    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form.save()

            # Reply to the contact person
            send_mail(
                'Your Query is received',
                'Thank you for your response....',  # message
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email_id']],
                fail_silently=False
            )

            # Send email to yourself
            send_mail(
                form.cleaned_data['subject'],
                f'From: {form.cleaned_data["email_id"]}\n{form.cleaned_data["message"]}',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False
            )

            messages.success(request, 'We will reach you soon')
            return redirect('product:contactus')

    context = {
        'form': form,
        'detail': log_user,
        'messages': messages.get_messages(request)
    }
    return render(request, 'product/contactus.html', context)


# def wishlist(request):
#     return render(request, 'product/wishlist.html')

def wishlist_add(request,product_id):
    product_id = ProductItem.objects.get(id=product_id)
    log_user = CustomUser.objects.get(pk=request.user.id)
    # customer_id = Customer.objects.filter(user_id=customer_id)
    # wish_list = WishListProduct.objects.filter()
    if WishListProduct.objects.filter(customer_id=log_user).filter(product_id=product_id).exists():
        messages.success(request,"Already exists in wishlist...")
        return redirect('product:wishlist_show')
    else:
        customer_id = CustomUser.objects.get(pk=request.user.id)
        add_product = WishListProduct.objects.create(customer_id=customer_id, 
                                             product_id=product_id)
        add_product.save()
        return redirect('product:wishlist_show')
    

def wishlist_show(request):
    login_user = CustomUser.objects.get(pk = request.user.id)
    user_id = CustomUser.objects.get(pk=request.user.id)
    wishlist_product = WishListProduct.objects.filter(customer_id= user_id)
    
    return render(request, 'product/wishlist.html',{'wishlist': wishlist_product,'detail': login_user,'messages': messages.get_messages(request)})

def delete_item(request, product_id):
    prod = WishListProduct.objects.get(pk=product_id)
    prod.delete()

    return redirect('product:wishlist_show')