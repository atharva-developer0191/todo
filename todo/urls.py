# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addTask/', views.addTask, name='addTask'),
]
