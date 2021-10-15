from django.db import models
import uuid

# Create your models here.
class RssChannel(models.Model):

    channel_uuid = \
        models.UUIDField(
            default=uuid.uuid4, unique=True, primary_key=True, editable=False
        )
    channel_source = \
        models.CharField(max_length=200, null=True, blank=True)