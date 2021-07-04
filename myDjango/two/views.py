from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse, path, re_path
# Create your views here.
def index(request):
    return HttpResponse(request.resolver_match.namespace)


def getStu(request):
    if request.resolver_match.namespace == "read":
        return HttpResponse("抱歉，您无权限查看此页面")
    elif request.resolver_match.namespace == "write":
        return HttpResponseRedirect(reverse("myapp:showStu"))
    else:
        return Http404("页面不存在")