from rest_framework import serializers
from tips.models import Tweet


class TweetSerializer(serializers.ModelSerializer):

    """ Returns JSON output for Tweet model """

    class Meta:
        model = Tweet
        fields = ['username', 'tip', 'email', 'created_at', 'updated']
