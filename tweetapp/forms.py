from django import forms
from twitteruserapp.models import CustomUser
from tweetapp.models import Tweet

class TweetForm(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea, max_length=140)

    

