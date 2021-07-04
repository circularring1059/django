from one import views
from django.contrib import admin
from django.urls import path, include

app_name = "one"  #反向url 起作用

urlpatterns = [
    path('index/', views.index, name="index"),
    path("getStu/", views.getStu),
]

