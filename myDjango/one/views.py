from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from one import models


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
    try:
        value = request.get_signed_cookie(key="one", salt="hello",)
        return HttpResponse("salt_cookie is {}".format(value,))
    except Exception as e:
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


def set_session(request):
    """
    可以有多个session  但只有一个sessionid,对于每个客户端，生成一条数据库记录，发生改变时，sessionid 不变，sessionData 改变
    session 不会重复设置，除非有更新或者被删除了
    """
    request.session["dir"] = "file"     #session 对象   会生成一个sessionid  放在cookie 里
    request.session["dir1"] = "file1"   #session 对象   会生成一个sessionid  放在cookie 里
    request.session["dir2"] = "file2"   #session 对象   会生成一个sessionid  放在cookie 里
    request.session["dir3"] = "file3"   #session 对象   会生成一个sessionid  放在cookie 里
    """
    global_settings
    
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
     
    SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
    SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
    SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
    SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
    SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
    SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
    SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
    """
    return HttpResponse("设置seesion成功")


def get_session(request):
    return HttpResponse(request.session.get("dir"))
    # return HttpResponse("hello")


def del_session(request):
    # try:
    #     del request.session["dir"]   # 删除单个session
    # except Exception as e:
    #     pass
    # request.session.clear()  #清空所有session 可重复操作
    request.session.flush()  #清空所有session和相应的seesionid  并且删除删除数据库相关记录 可重复操作
    return HttpResponse("删除session")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        print(88)
        if request.POST.get("name") and request.POST.get("passwd"):
            models.User.create(request.POST.get("name"), request.POST.get("passwd"))
            return render(request, "token_login.html")
        else:
            return render(request, "register.html", {"msg":"输入不合法"})
