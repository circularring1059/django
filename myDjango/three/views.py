from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class AboutView(TemplateView):
    template_name = "three-about.html"

def login(request):
    # return HttpResponse("login")
    return render(request, 'three-login.html')

def register(request):
    # return HttpResponse("register")
    return render(request, "three-register.html")

def logout(request):
    # return HttpResponse("logout")
    return render(request, "three-logout.html")
