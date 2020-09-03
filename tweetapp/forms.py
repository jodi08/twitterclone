from django import forms
from twitteruserapp.models import CustomUser
from tweetapp.models import Tweet

class TweetForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Tweet.objects.all())
    tweet = forms.CharField(max_length=140)

    

