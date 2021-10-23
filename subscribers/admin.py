from django.contrib import admin

# Register your models here.
from .models import Subscriber, InterestKeyword

admin.site.register(Subscriber)
admin.site.register(InterestKeyword)