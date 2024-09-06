from django import forms
from django.core.exceptions import ValidationError

from .models import Notification


class NewLaterForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        check = Notification.objects.filter(email = email)

        if check.exists():
            raise ValidationError('Email is allready')
        return email
    
class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.TextInput())

    