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
    import datetime
    response = HttpResponse("set_salt_cookie")
    response.set_signed_cookie(key="one", value="two", salt="hello", expires=datetime.datetime.now()+datetime.timedelta(days=2), path="/" )  #设置两天后过期
    return response


def get_salt_cookie(request):
    value = request.get_signed_cookie(key="one", salt="hello",)
    # one = request.get_signed_cookie("one", salt="hello")
    if value:
        return HttpResponse("salt_cookie is {}".format(value,))
    return HttpResponse("获取salt_cookie失败")


def login(request):

    login_info = request.COOKIES.get("login", None)
    if login_info:
        name, passwd = login_info.split("-")
        print(name, passwd)
    else:
        pass
    if request.method == "GET":
        return render(request, "one_login.html", locals())
    else:
        if request.POST.get("name") == "ring" and request.POST.get("passwd") == "yuan":
            # response = HttpResponse("登入成功")
            response = HttpResponse()
            if request.POST.get("flag"):
                response.set_cookie("login", request.POST.get("name")+"-"+request.POST.get("passwd"), max_age=3600, path="/" )
                response.content="登入成功，记住密码"
                return response
            response.delete_cookie("login")
            response.content="登入成功，不记住密码"
            return response
    response = HttpResponse("登入失败")
    # response.content("fail")
    response.delete_cookie("login")
    return response