from django.shortcuts import render, HttpResponseRedirect, reverse
from tweetapp.forms import TweetForm
from tweetapp.models import Tweet
from twitteruserapp.models import CustomUser
# Create your views here.

def tweet_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                tweet = data.get('tweet'),
                author = request.user,  
            )
            return HttpResponseRedirect(reverse("homepage"))
        

    form = TweetForm()
    return render(request, "recipe_form.html", {"form": form})
