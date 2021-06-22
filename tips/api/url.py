from django.urls import path, include
from django.conf.urls import url
from .views import TweetListApiView

urlpatterns = [
    path('', TweetListApiView.as_view()),
]