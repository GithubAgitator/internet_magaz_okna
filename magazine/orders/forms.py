from django import forms
from .models import Order
from .models import *

class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)

class OrderCreateForm(forms.ModelForm):
    class Meta:
        madel = Order
        fields = ['user', 'total_price', 'customer_name', 'customer_phone']

