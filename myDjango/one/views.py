from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    # return HttpResponse("index")
    return render(request, "one_index.html")


def getStu(request):
    return render(request, "one_getStu.html")
    # return HttpResponseRedirect(reverse("myapp:showClass"))
    # return HttpResponseRedirect(reverse("myapp:showStu"))
    # print(reverse("myapp:showClass"))  #/myapp/showClass/
    # return HttpResponseRedirect(reverse("myapp:editStu", args=(2,)))   #args  传参


def set_cookie(request):
     response =  HttpResponse("set_cookie")
     response.set_cookie("ring", "yuan", max_age=24*60*60, path="/")
     return response


def get_cookie(request):
    ring = request.COOKIES.get("ring")
    if ring:
        return HttpResponse("cookie is {}".format(ring,))
    return HttpResponse("cookie is not exist")

def set_salt_cookie(request):
    response = HttpResponse("set_salt_cookie")
    response.set_signed_cookie(key="one", value="two", salt="hello",max_age=24*60*60, path="/" )
    return response


def get_salt_cookie(request):
    value = request.get_signed_cookie(key="one", salt="hello")
    # one = request.get_signed_cookie("one", salt="hello")
    if value:
        return HttpResponse("salt_cookie is {}".format(value,))
    return HttpResponse("获取salt_cookie失败")