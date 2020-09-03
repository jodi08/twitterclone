from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from authenticationapp.forms import LogInForm
from twitteruserapp.models import CustomUser

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user: 
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
            
    form = LogInForm()
    return render(request, "login.html", {"form": form})
    return HttpResponse('login')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

