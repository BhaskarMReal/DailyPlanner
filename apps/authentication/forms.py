from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput, help_text=None)
    password2 = forms.CharField(label='Enter password', widget=forms.PasswordInput, help_text=None)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

        help_texts = {
            "username":None,
            'email':None,
        }
       