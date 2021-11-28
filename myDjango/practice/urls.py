from django.urls import path

from . import views
app_name = "practice"

urlpatterns = [
    path('list_books/', views.list_book, name="list_book" )
]