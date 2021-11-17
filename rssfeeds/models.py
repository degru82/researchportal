from django.db import models
import uuid

from subscribers.models import Subscriber

# Create your models here.
class RssFeed(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    feed_image = models.ImageField(
        null=True, blank=True, default='rssfeed.png', upload_to='rssfeeds'
    )
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    created_by = models.ForeignKey(Subscriber, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    # feed_items = models.ManyToOneRel()

class FeedItem(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2000, null=True, blank=True)
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    feed_belongs_to = models.ForeignKey(
        RssFeed, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.title