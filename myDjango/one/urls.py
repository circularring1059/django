from one import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('index/', views.index),
]

