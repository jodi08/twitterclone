from django.shortcuts import render, HttpResponseRedirect, reverse
from twitterclone.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required
from twitteruserapp.models import CustomUser
from twitteruserapp.forms import  CustomUserCreationForm
from django.contrib.auth import login


# Create your views here.
@login_required
def index_view(request):
    return render(request, "index.html", {'auth_user_model': AUTH_USER_MODEL})

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(username=data.get("username"), password=data.get("password"), displayname = data.get("displayname"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = CustomUserCreationForm()
    return render(request, 'signup.html', {"form": form})

def userprofile_view(request):
    return render(request, 'userprofile.html')
    