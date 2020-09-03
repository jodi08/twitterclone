# Generated by Django 3.0.9 on 2020-09-03 16:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruserapp', '0002_auto_20200902_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
