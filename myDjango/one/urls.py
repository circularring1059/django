from one import views
from django.contrib import admin
from django.urls import path, include

app_name = "one"  #反向url 起作用

urlpatterns = [
    path('index/', views.index, name="index"),
    path("getStu/", views.getStu),
    path("set_cookie/", views.set_cookie),
    path("get_cookie/", views.get_cookie),
    path("set_salt_cookie/", views.set_salt_cookie),
    path("get_salt_cookie/", views.get_salt_cookie),
]

