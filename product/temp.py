from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from product.models import ProductItem
from .models import Cart
from .forms import CartUpdateForm, CartRemoveForm
from authsystem.models import CustomUser


# Create your views here.
def product(request):

    product = ProductItem.objects.all()
    context = {
        'product': product
    }
    return render(request, 'product/product.html',context)


def category(request, val):

    product = ProductItem.objects.filter(CATAGORY_CHOICES=val)
    title = ProductItem.objects.filter(CATAGORY_CHOICES=val).values('P_name')
    context = {
        'val': val,
        'product': product,
        'title': title,
    }
    return render(request, 'product/category.html', context)

def productdetail(request, id):
    pro = ProductItem.objects.get(pk=id)
    context = {
        'pro': pro
    }

    return render(request, 'product/productdetail.html',context)

def test(request):
   return render(request, 'product/test.html')

def carttest(request):
   return render(request, 'product/carttest.html')




def add_to_cart(request, prod_id):
    user = request.user
    product = get_object_or_404(ProductItem, id=prod_id)

    # Check if the product is already in the cart
    if Cart.objects.filter(user_id=user, product_id=product).exists():
        messages.warning(request, 'This item is already in your cart.')
    else:
        Cart(user_id=user, product_id=product).save()
        messages.success(request, 'Item added to your cart successfully.')

    return redirect('product:showcart')


def showcart(request):
    user = request.user
    cart_items = Cart.objects.filter(user_id=user)
    total = sum(item.total_cost for item in cart_items)

    if request.method == 'POST':
        if 'update_quantity' in request.POST:
            form = CartUpdateForm(request.POST, instance=request.user.cartitems.first())
            if form.is_valid():
                form.save()
                # Optionally, you can add a success message here
                return redirect('product:showcart')
        elif 'remove_item' in request.POST:
            remove_form = CartRemoveForm(request.POST)
            if remove_form.is_valid():
                cart_item_id = remove_form.cleaned_data['cart_item_id']
                Cart.objects.filter(id=cart_item_id).delete()
                # Optionally, you can add a success message here
                return redirect('product:showcart')
    else:
        form = CartUpdateForm()
        remove_form = CartRemoveForm()

    return render(request, 'product/addtocart.html', {'cart_items': cart_items, 'form': form, 'remove_form': remove_form, 'cart': cart_items, 'total': total})


#-----------------------------------------------------------------------------
# def add_to_cart(request, prod_id):
#     user = request.user
#     product = get_object_or_404(ProductItem, id=prod_id)
#     Cart(user_id=user, product_id=product).save()
#     return redirect('product:showcart')


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


#-----------------------------------------------------------------------------


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