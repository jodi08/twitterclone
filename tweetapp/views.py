from django.shortcuts import render, HttpResponseRedirect, reverse
from tweetapp.forms import TweetForm
from tweetapp.models import Tweet
from twitteruserapp.models import CustomUser
from notificationapp.models import Notification
import re
from django.views.generic import TemplateView
# Create your views here.

# def tweet_view(request):
#     if request.method == "POST":
#         form = TweetForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             tweet_post = Tweet.objects.create(
#                 tweet = data.get('tweet'),
#                 author = request.user,  
#             )
#             if "@" in data['tweet']:
#                 recipient = re.findall(r'@(\w+)', data.get("tweet"))
#                 for post in recipient:
#                     message = Notification.objects.create(msg_content=tweet_post, receiver=CustomUser.objects.get(username=post))
#                 return HttpResponseRedirect(reverse("homepage"))
        

#     form = TweetForm()
#     return render(request, "tweet.html", {"form": form})

class TweetFormView(TemplateView):

    def get(self, request):
        form = TweetForm()
        return render(request, "tweet.html", {"form": form})

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet_post = Tweet.objects.create(
                tweet = data.get('tweet'),
                author = request.user,  
            )
            if "@" in data['tweet']:
                recipient = re.findall(r'@(\w+)', data.get("tweet"))
                for post in recipient:
                    message = Notification.objects.create(msg_content=tweet_post, receiver=CustomUser.objects.get(username=post))
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "tweet.html", {"form": form})




# def tweet_detail(request, tweet_id):
#     my_tweet = Tweet.objects.filter(id=tweet_id).first()
#     return render(request, 'tweet_detail.html', {'tweet': my_tweet})

class TweetDetail(TemplateView):

    def get(self, request, tweet_id):
        my_tweet = Tweet.objects.filter(id=tweet_id).first()
        return render(request, 'tweet_detail.html', {'tweet': my_tweet})


