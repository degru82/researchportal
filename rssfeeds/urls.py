from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcomePageView, name='welcome-page'),
    path('channel/', views.show_channels, name='channel-list'),
    path('channel/new', views.enroll_channel, name='new-channel'),
    path('channel/<str:channel_id>/', views.show_singlechannel, name='channel-detail'),
    path('channel/update/<str:channel_id>/', views.update_channel, name='update-channel'),
    path('channel/delete/<str:channel_id>/', views.delete_channel, name='delete-channel'),
]
