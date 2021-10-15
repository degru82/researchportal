from django.urls import path
from . import views

urlpatterns = [
    path('channels/', views.show_channels, name='show-channels'),
]