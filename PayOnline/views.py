from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import razorpay
from product.models import OrderItem 
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from authsystem.models import CustomUser
# from weasyprint import HTML
from .models import Pay
import json
def first(request):
    return render(request,'PayOnline/first.html')

def home(request):
    order_item = OrderItem.objects.last()
    log_user = CustomUser.objects.get(pk = request.user.id)
    context = {
        
        'order_item' : order_item,
        'detail': log_user,
     }
    if request.method == "POST":
        name = request.POST.get('name')
        amount =float(request.POST.get('amount'))*100
        email=request.POST.get('email')
        client = razorpay.Client(auth =("rzp_test_ifqXZb84qSL1CP" , "IwSyyaBvXh300nlqM0kqb0ow"))
        payment = client.order.create({'amount':amount, 'currency':'INR',
                              'payment_capture':'1' })
        
        info = Pay(name = name , amount =amount , order_id = payment['id'])
        info.save()
        
        return render(request, 'PayOnline/index.html' ,{'payment':payment})
    return render(request, 'PayOnline/index.html',context)


@csrf_exempt
def success(request):
    
    
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key , val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
    
        user = Pay.objects.filter(order_id = order_id).first()
        user.paid = True
        user.save()
        
        msg_plain=render_to_string('PayOnline/email.txt')
        msg_html=render_to_string('PayOnline/email.html')

        # send_mail("Your donation has been received",msg_plain,settings.EMAIL_HOST_USER,
        #             ["rajlogicrays@gmail.com"],# [user.email],
        #             html_message=msg_html)

    return render(request, "PayOnline/success.html")


# def download_orders(request):
#     #add your invoice url here
#     full_url = request.build_absolute_uri(reverse('orders'))
#     html = HTML(url=full_url)
#     html.write_pdf(target='C:/Users/Asus/Desktop/download/orders.pdf')

#     fs = FileSystemStorage('C:/Users/Asus/Desktop/download')
#     with fs.open('orders.pdf') as pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="orders.pdf"'
#         return response
#     return response