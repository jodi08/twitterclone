from django.urls import path

"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index_view, name='homepage'),
    path('signup/', views.signup_view, name="signup"),
    path('userprofile/', views.userprofile_view, name="profile"),
    path('userdetail/<int:user_id>/', views.userdetails_view, name="user_details"),
    path('follow/<int:user_id>/', views.follow_view, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow_view, name='unfollow'),
]
