from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_people, name='subscriber-list'),
    path('people/', views.show_people, name='subscriber-list'),
    path('interests/', views.show_interest, name='interest-list'),
]
