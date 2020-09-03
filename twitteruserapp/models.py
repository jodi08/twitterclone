from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import auth


# Create your models here.
class CustomUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False)
    displayname = models.CharField(max_length=75, blank=True, null=True)
    


    def __str__(self):
        return "@{}".format(self.username)