from django import forms
from twitteruserapp.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LogInForm(forms.Form):
    username = forms.CharField(max_length=240, initial="")
    password = forms.CharField(widget=forms.PasswordInput, initial="")

