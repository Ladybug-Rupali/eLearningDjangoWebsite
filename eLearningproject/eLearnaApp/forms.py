from django import forms
from .models import EmailInput

class EmailInputForm(forms.ModelForm):
    class Meta:
        model = EmailInput
        fields = ['email']
