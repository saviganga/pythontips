from django.forms import ModelForm
from .models import Tweet

class PostTipsForm(ModelForm):

    class Meta:
        model = Tweet
        fields = ['username', 'tip', 'email',]