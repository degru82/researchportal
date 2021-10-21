from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcomePageView, name='welcome-page'),
    path('channel/', views.show_channels, name='channel-list'),
    path('channel/<str:link_id>/', views.show_singlechannel, name='channel-detail')
]
