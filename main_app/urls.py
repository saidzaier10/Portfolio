from django.urls import path, include
from django import views
from . import views

urlpatterns = [
    path ('main_app/templates/', views.home, name='home'), 
]
