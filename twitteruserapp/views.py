from django.shortcuts import render, HttpResponseRedirect, reverse
from twitterclone.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required
from twitteruserapp.models import CustomUser
from twitteruserapp.forms import  CustomUserCreationForm
from django.contrib.auth import login
from tweetapp.models import Tweet
from notificationapp.models import Notification



# Create your views here.
@login_required
def index_view(request):
    tweets = Tweet.objects.all()
    tweet_count = Tweet.objects.filter(author=request.user).count() #Helped by Howard Post
    following = request.user.followers.all()
    notification_count = Notification.objects.filter(receiver=request.user, notification_flag=False).count()
    return render(request, "index.html", {'tweets': tweets, "tweet_count": tweet_count, "following": following, 'notification_count': notification_count})

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
    user_profile = request.user
    user_tweets = Tweet.objects.filter(author=user_profile.id)
    tweet_count = Tweet.objects.filter(author=request.user).count()
    return render(request, 'userprofile.html', {'user_profile': user_profile, 'user_tweets': user_tweets, 'tweet_count': tweet_count})

def userdetails_view(request, user_id):
    my_tweeter = CustomUser.objects.filter(id=user_id).first()
    tweet_count = Tweet.objects.filter(author=request.user).count()
    user_tweets = Tweet.objects.filter(author=my_tweeter.id)
    following = request.user.followers.all()
    return render(request, 'userdetail.html', {'tweeter': my_tweeter, 'tweets': user_tweets, "following": following, 'tweet_count': tweet_count})

#helped by Jessica Benson
def follow_view(request, user_id):
    request.user.followers.add(CustomUser.objects.get(id=user_id))
    return HttpResponseRedirect(reverse("homepage"))

#helped by Jessica Benson
def unfollow_view(request, user_id):
    request.user.followers.remove(CustomUser.objects.get(id=user_id))
    return HttpResponseRedirect(reverse("homepage"))
    
