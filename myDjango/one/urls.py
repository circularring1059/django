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
    path("set_session/", views.set_session),
    path("get_session/", views.get_session),
    path("del_session/", views.del_session),
    path("login/", views.login),
    path("register/", views.register),
    path("token_login/", views.token_login),
]

