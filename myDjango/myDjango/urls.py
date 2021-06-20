"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from app01 import views

def login(request):
    li = ["python", "golang", "shell", "java"]
    dc = {"a":1, "b":"c"}
    print(request.GET)  #获取URL传值
    if request.method == "GET":
        print(request.method)
        # return HttpResponse("hello Django")
        print(locals())
        return render(request, 'login.html', locals())
    else:
        print(request.method)
        print(request.POST.get("username"))
        print(request.POST.get("passwd"))
        if request.POST.get("passwd") =="123"  and request.POST.get("passwd") == "123":
            return redirect("https://www.baidu.com")
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})   #locals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('getClass/', views.getClass),
    path('addClass/', views.addClass),
    path('delClass/', views.delClass),
    path('editClass/', views.editClass),

]
