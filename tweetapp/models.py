from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class TwitterUser(AbstractUser):
    pass

class Tweet(models.Model):
    pass

class Notifications(models.Model):
    pass
