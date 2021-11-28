from django.urls import path

from . import views
app_name = "practice"

urlpatterns = [
    path('list_books/', views.list_book, name="list_book" ),
    path('show_form/', views.show_form, name="show_form" ),
]