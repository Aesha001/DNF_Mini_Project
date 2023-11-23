from django.shortcuts import render
from authsystem.models import CustomUser
from django.contrib.auth.decorators import login_required
from product.models import ProductItem
# Create your views here.

@login_required(login_url='authsystem:login')
def core(request):
   
    log_user = CustomUser.objects.get(pk = request.user.id)


    context = {
        'detail': log_user,
   
       
    }
    return render(request,'core/home.html',context)

def aboutus(request):
    log_user = CustomUser.objects.get(pk = request.user.id)
    context = {
        'detail': log_user,
    }
    return render(request,'core/aboutus.html',context) 

# def contactus(request):
#     log_user = CustomUser.objects.get(pk = request.user.id)
#     context = {
#         'detail': log_user,
#     }
#     return render(request,'core/contactus.html',context)


def blog(request):
    log_user = CustomUser.objects.get(pk = request.user.id)
    context = {
        'detail': log_user,
    }
    return render(request,'core/blog.html',context)


def search(request):
    query = request.GET.get('query','') # Use request.GET.get('query', '') to get the 'query' parameter value with a default empty string
    print(type(query))
    if not query:
        pass
    else:
        log_user = CustomUser.objects.get(pk = request.user.id)
        product = ProductItem.objects.filter(P_name__icontains=query)
        context = {
            'product': product,
            'detail': log_user,
        }
        return render(request,'core/search.html',context)
    return render(request,'core/search.html')

@login_required(login_url='authsystem:login')
def profile(request):
    log_user = CustomUser.objects.get(pk = request.user.id)

    print(log_user)
    context = {
        'detail': log_user,
    }
    return render(request,'core/profile.html',context)
    