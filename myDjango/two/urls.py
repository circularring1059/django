from django.urls import path, re_path
from . import views

app_name ="two"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('getStu/', views.getStu, name="getStu"),
    path('goto/', views.goto, name="goto"),
    path('getCar/', views.getCar, name="getCar"),
    path("login/", views.loginViews.as_view(), name="login"),

]