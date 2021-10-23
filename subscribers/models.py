from django.db import models
import uuid

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    personal_interests = models.ManyToManyField(
        'InterestKeyword', blank=True, null=True
    )

    def __str__(self):
        return self.name


class InterestKeyword(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name

