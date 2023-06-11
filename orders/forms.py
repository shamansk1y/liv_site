from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'type': "text", 'class': "form-control", 'id': "first_name", 'name': "first_name", 'value': ""}))

    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'type': "text", 'class': "form-control", 'id': "last_name", 'name': "last_name", 'value': ""}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': "text", 'class': "form-control", 'id': "email", 'name': "email", 'value': ""}))

    phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'type': "text", 'class': "form-control", 'id': "phone", 'name': "phone", 'value': ""}))

    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control", 'id': "city", 'name': "city", 'value': ""}))

    postal_code = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
    'type': "text", 'class': "form-control", 'id': "postal_code", 'name': "postal_code", 'value': ""}))

    message = forms.CharField(max_length=300, required=False, widget=forms.Textarea(attrs={
    'type': "text", 'class': "form-control", 'id': "message", 'name': "message", 'value': ""}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'postal_code', 'message']
