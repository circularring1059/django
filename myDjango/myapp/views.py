from django.shortcuts import render, redirect
from django.urls import path, re_path
from django.http import HttpResponse, Http404
from myapp import models
# Create your views here.
def index(request):
    # return HttpResponse("myapp_index")
    return render(request, "myapp_index.html")

def showStu(request):
    stu_list = models.Student.objects.all()
    return render(request, "showStu.html", locals())


def addStu(request):
    # stu_list = ["桃子", "李子", "香蕉", "葡萄", "荔枝", "芒果", "西瓜"]
    # for stu in stu_list:
    #    models.Student.objects.create(stu_name=stu)
    if request.method == 'GET':
        class_list  = models.Class.objects.all()
        print(locals())
        for i in  class_list:
            print(i.id, i.class_name)
        return render(request, "addStu.html",locals())
    else:
        models.Student.objects.create(stu_name=request.POST.get("stu_name"), sc_id=request.POST.get("class_id"))
        return redirect("/myapp/showStu")

def editStu(request, stu_id):
    if request.method == "GET":
        stu = models.Student.objects.all().filter(id=stu_id).first()
        class_list = models.Class.objects.all()
        return render(request, "editStu.html",locals())
    else:
        models.Student.objects.all().filter(id=stu_id).update(stu_name=request.POST.get("stu_name"), sc_id=request.POST.get("sc_id"))
        return redirect("/myapp/showStu")

def delStu(request, stu_id):
    # return HttpResponse("学生{}删除成功".format(stu_id))
    models.Student.objects.all().filter(id=stu_id).delete()
    return redirect("/myapp/showStu/")