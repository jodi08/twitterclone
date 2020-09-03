from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(max_length=20)
    displayname = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    