from django.db import models
from django.utils.timezone import now
from twitteruserapp.models import CustomUser


# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    timestamp = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp']
    

    def __str__(self):
        return self.tweet
    
    


