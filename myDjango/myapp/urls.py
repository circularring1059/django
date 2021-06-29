from django.urls import path, re_path
from myapp import views

urlpatterns = [
    path('index/', views.index),
    path('showStu/', views.showStu),
    path('addStu/', views.addStu, name="addStu"),
    path('delStu/<int:stu_id>/', views.delStu, name="delStu"),
]