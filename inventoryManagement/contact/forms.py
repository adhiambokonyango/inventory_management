from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firstName', 'secondName', 'PFnumber', 'Ministry', 'Department', 'email')
