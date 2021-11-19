from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_channels, name='channel-list'),
    path('new', views.enroll_channel, name='new-channel'),
    path(
        '<str:channel_id>',
        views.show_singlechannel,
        name='channel-detail'
    ),
    path(
        'update/<str:channel_id>/',
        views.update_channel,
        name='update-channel'
    ),
    path(
        'delete/<str:channel_id>/',
        views.delete_channel,
        name='delete-channel'
    ),
]
