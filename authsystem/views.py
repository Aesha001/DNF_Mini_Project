from django.shortcuts import redirect,render
from django.forms.forms import Form
from authsystem.forms import registeruser,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.forms import PasswordResetForm
from .models import CustomUser
from .forms import registeruser

# Create your views here.

def logview(request):
    return render(request,'authsystem/login.html')


def myregister(request):
    return render(request,'authsystem/register.html')






def forgot_password(request):
    if request.method=="POST":
        email=request.POST.get('email')
        query_set=CustomUser.objects.filter(email=email)
        print(query_set)
        if registeruser.email==email:
            return redirect("/")
    return render(request,'authsystem/forgot_password.html')






def register_user(request):
    print('register_user called')
    if request.method == 'POST':
        print('this is post request')
        form = registeruser(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Registered Sucessfully!!")
            return redirect('authsystem:login')
        else:
            messages.error(request,'Form validation error')
    else:
        form = registeruser()
    return render(request,'authsystem/register.html',{'form':form,'messages': messages.get_messages(request)})




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('core:home')
        else:
            messages.error(request, "Username or Password is incorrect")
            return redirect('authsystem:login')

    form = LoginForm()
    return render(request, 'authsystem/login.html', {'form': form, 'messages': messages.get_messages(request)})

def logout_user(request):
    logout(request)
    return redirect('authsystem:login')