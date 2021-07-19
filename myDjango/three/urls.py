from one import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import  *
app_name = "three"  #反向url 起作用




urlpatterns = [
    path('index/', TemplateView.as_view(template_name="three-index.html"),name="index"),
    path('about/', AboutView.as_view(), name="about")
]
