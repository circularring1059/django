from django.shortcuts import render, redirect
from django.urls import path, re_path
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):

    return HttpResponse("myapp_index")