from django.urls import path, re_path
from . import views

app_name ="two"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('getStu/', views.getStu, name="getStu"),

]