from django.contrib import admin

# Register your models here.
from .models import RssFeed, FeedItem

admin.site.register(RssFeed)
admin.site.register(FeedItem)