from django.urls import path
from authsystem import views
from .forms import LoginForm,MyPasswordResetForm,MySetPasswordForm
from django.contrib.auth import views as auth_view



app_name = 'authsystem'
urlpatterns = [
  
     # path('login/',views.logview),
     # path('register/',views.regview),
     path('myregister/',views.register_user,name='myregister'),
     path('login_user/',views.login_user,name='login'),
     path('forgot_password/',views.forgot_password,name='forgot_password'),
     path('logout_user/',views.logout_user,name='logout'),
     
     
     #forgot-password
     path('password-reset/',auth_view.PasswordResetView.as_view(template_name='authsystem/password_reset.html',form_class=MyPasswordResetForm),name="password_reset"),
     
     path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='authsystem/password_reset_done.html'),name="password_reset_done"),
     
     path('password-reset-confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='authsystem/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
     
     path('password-reset-complete',auth_view.PasswordResetCompleteView.as_view(template_name='authsystem/password_reset_complete.html'),name='password_reset_complete'),
     
]