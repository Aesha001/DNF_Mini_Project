from django.shortcuts import render, redirect
from .forms import MailForm
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def mail_function(request):
    form = MailForm()
    
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            to_mail = form.cleaned_data.get('email_id')
            
            form.save()
            msg = "Thanks for the Inquiry"
            
            send_mail(msg,
                subject, #'Subject here',
                message, #'Here is the message.',
                settings.EMAIL_HOST_USER, #'from@example.com',
            
                [to_mail ],
                fail_silently=False,
            )
            
            send_mail(
                subject, #'Subject here',
                message, #'Here is the message.',
                settings.EMAIL_HOST_USER, #'from@example.com',
            
                [settings.EMAIL_HOST_USER ],
                 fail_silently=False,
            )
            return redirect('mailapp:thanks')
    context = {
        'form' : form
    }
    return render(request, 'mail/index.html', context=context)

def thanks_function(request):
    return render(request, 'mail/thanks.html')
