from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse, path, re_path
# Create your views here.
from two import models
from django.views import View
from .form import *

def index(request):
    return HttpResponse(request.resolver_match.namespace)


def getStu(request):
    if request.resolver_match.namespace == "read":
        return HttpResponse("抱歉，您无权限查看此页面")
    elif request.resolver_match.namespace == "write":
        return HttpResponseRedirect(reverse("myapp:showStu"))
    else:
        return Http404("页面不存在")


def goto(request):
    return HttpResponseRedirect(reverse("two:index", current_app="read"))  #反向url


def getCar(request):
    car_list = models.Car.objects.all()
    print(car_list)
    return HttpResponse(car_list)


#from 表单
class loginViews(View):
    def get(self, request):
        stu_name = StuForm()
        return render(request, "stu_login.html", locals())
        # return HttpResponse(stu_name)
    def post(self, requet):
        stu_name = requet.POST.get("stu_name")
        form_stu_name = StuForm(stu_name)
        # print(form_stu_name)
        if form_stu_name.is_valid():
            print(form_stu_name.cleaned_data())
            # if form_stu_name.clean().get("stu_name") == "桃子":
            #     return HttpResponse("登入成功")
        return HttpResponse("登入失败")