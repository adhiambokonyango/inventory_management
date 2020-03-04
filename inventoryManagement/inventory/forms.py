from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('type', 'price', 'status', 'issues')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('type', 'price', 'status', 'issues')


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('type', 'price', 'status', 'issues')

    # LOGIN

    def clean(self):
        cleaned_data = self.cleaned_data
        password_one = self.cleaned_data.get('password_first')
        password_two = self.cleaned_data.get('password_again')
        if password_one != password_two:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("The username you've chosen is unavailable.")
        return username

    def clean_email(self):
        email_address = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email_address)
        if qs.exists():
            raise forms.ValidationError("The email address you've chosen is already registered.")
        return email_address
