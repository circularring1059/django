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

