from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcomePageView, name='welcome-page'),
    path('channels/', views.show_channels, name='show-channels'),
    path('channels/ch/', views.show_singlechannel, name='show-singlechannel')
]
