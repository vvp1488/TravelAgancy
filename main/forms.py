from django import forms
from .models import Order


class OrderForm(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=9)
