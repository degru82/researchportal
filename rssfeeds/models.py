from django.db import models
import uuid

# Create your models here.
class RssFeed(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.title

    # feed_items = models.ManyToOneRel()

class FeedItem(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2000, null=True, blank=True)
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=100)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
