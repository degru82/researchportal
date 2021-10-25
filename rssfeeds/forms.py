from django.forms import ModelForm
from .models import RssFeed

class RssFeedForm(ModelForm):
    class Meta:
        model = RssFeed
        fields = '__all__'