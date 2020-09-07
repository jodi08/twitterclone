from django.db import models
from twitteruserapp.models import CustomUser
from tweetapp.models import Tweet


class Notification(models.Model):
     receiver =  models.ForeignKey(CustomUser, related_name="receiver", on_delete=models.CASCADE, blank=True, null=True)
     msg_content = models.ForeignKey(Tweet, on_delete=models.CASCADE, blank=True, null=True)
     notification_flag = models.BooleanField(default=False)


     