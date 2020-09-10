from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    signup_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'displayname']

admin.site.register(CustomUser, CustomUserAdmin)
