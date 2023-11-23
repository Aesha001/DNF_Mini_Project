# forms.py
from django import forms
from .models import Cart, Order,Contact_page
from django.forms import inlineformset_factory
from authsystem.models import CustomUser



class ContactCreation(forms.ModelForm):
    class Meta:
        model = Contact_page
        fields = ['your_name', 'Email', 'subject', 'text']

class CartUpdateForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']


class CartRemoveForm(forms.Form):
    cart_item_id = forms.IntegerField(widget=forms.HiddenInput())
    # Optionally, you can add other fields if needed




CartUpdateFormSet = inlineformset_factory(CustomUser, Cart, fields=('quantity',), can_delete=False)



class OrderCreateForm(forms.ModelForm):
    Full_name = forms.CharField(label='Enter Your Full Name', max_length=100 ,
                                          widget=forms.TextInput
                                        (attrs={'class': "form-control"}))
   

    address = forms.CharField(label='Enter Your Deliverd Address', max_length=100,
                                          widget=forms.Textarea
                                        (attrs={'class': "form-control"}))
                                    
    city = forms.CharField(label='Enter Your City', max_length=100 ,
                                          widget=forms.TextInput
                                        (attrs={'class': "form-control"}))

    class Meta:
        model = Order
        fields = ['Full_name', 'email', 'address', 'city']

# class CartRemoveForm(forms.Form):
#     cart_item_id = forms.IntegerField(widget=forms.HiddenInput())

# class CartRemoveForm(forms.ModelForm):
#     class Meta:
#         model = Cart
#         fields = ['id']  # Add other fields if needed
