from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):

    username = models.CharField(max_length=140, blank=False, null=False)
    tip = models.CharField(max_length=140, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(max_length=100, auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.tip}'


class MyUser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tips = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='author', blank=True, null=True)

    def __str__(self):
        return f'{self.user}'
