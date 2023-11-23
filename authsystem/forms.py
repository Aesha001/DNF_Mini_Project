from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,SetPasswordForm,PasswordChangeForm,PasswordResetForm
from .models import CustomUser

class registeruser(UserCreationForm):
     username = forms.CharField( label='Username', max_length=100 ,
                                         widget=forms.TextInput
                                         (attrs={'class': "form-control"}))
     
     first_name = forms.CharField(label='First name', max_length=100 ,
                                         widget=forms.TextInput
                                         (attrs={'class': "form-control"}))

    
     last_name = forms.CharField(label='Last name', max_length=100 ,
                                         widget=forms.TextInput
                                         (attrs={'class': "form-control"}))
     
     


    #  area_name = forms.CharField(label='Area name', max_length=100 ,
    #                                      widget=forms.TextInput
    #                                      (attrs={'class': "form-control"})) 

     
     
     email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'class': "form-control",'autocomplete': 'email'})
    )
     fields = ['email']
     labels = {'email':'Email ID'}
     widget = {
      'email':forms.EmailInput(attrs={'class':'form-control'}),
     }
     
     password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': "form-control",'autocomplete': 'new-password'}),
        # help_text=password_validation.password_validators_help_text_html(),
          )
     password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': "form-control",'autocomplete': 'new-password'}),
        strip=False,
        # help_text=_("Enter the same password as before, for verification."),
     )
    #  pin_code = forms.CharField(label='Pincode', max_length=100 ,
    #                                      widget=forms.TextInput
    #                                      (attrs={'class': "form-control"})) 


     contact = forms.CharField(label='Contact', max_length=10 ,
                                         widget=forms.TextInput
                                         (attrs={'class': "form-control"}))
     
     address = forms.CharField(label='Address', max_length=100 ,
                                         widget=forms.TextInput
                                         (attrs={'class': "form-control"})) 
          

     class Meta:
          model = CustomUser
          fields = ['username','first_name','last_name','email','password1','password2','contact','address']
         

class LoginForm(AuthenticationForm):
       username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control" ,'autofocus': True,}))

       password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':"form-control" ,'autocomplete': 'current-password'}),
    )
       

class Meta:
        model = CustomUser
        fields = ['username','password']
        
class MySetPasswordForm(SetPasswordForm):
   new_password1 = forms.CharField(label='New Password: ',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})
   )
   new_password2 = forms.CharField(label='Confirm New Password: ',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})
   )
   
class MyPasswordResetForm(PasswordResetForm):
   email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'})) 