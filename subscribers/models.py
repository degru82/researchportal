from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Subscriber(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True,
        upload_to='subscribers/',
        default='profile.png'
    )
    personal_interests = models.ManyToManyField(
        'InterestKeyword', blank=True, null=True
    )

    def __str__(self):
        return str(self.user.username)


class InterestKeyword(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name

