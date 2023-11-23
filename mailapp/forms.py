from django import forms 
from .models import MailBox

class MailForm(forms.ModelForm):
    class Meta:
        model = MailBox
        fields = "__all__"