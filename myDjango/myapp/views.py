from django.shortcuts import render, redirect
from django.urls import path, re_path
from django.http import HttpResponse, Http404
from myapp import models
def index(request):
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
        try:
            stu = models.Student.objects.all().get(id=stu_id)
        except Exception as e:
            return HttpResponse("该学生不存在")
        class_list = models.Class.objects.all()
        return render(request, "editStu.html", locals())
    else:
        models.Student.objects.all().filter(id=stu_id).update(stu_name=request.POST.get("stu_name"), sc_id=request.POST.get("sc_id"))
        return redirect("/myapp/showStu")

def delStu(request, stu_id):
    # return HttpResponse("学生{}删除成功".format(stu_id))
    models.Student.objects.all().filter(id=stu_id).delete()
    return redirect("/myapp/showStu/")


def showClass(request):
    class_list = models.Class.objects.all()
    return render(request,"showClass.html", locals())


def addClass(request):
    if request.method == "GET":
        return render(request, "addClass.html")
    else:
        print(request.POST.get("class_name"))
        if models.Class.objects.all().filter(class_name=request.POST.get("class_name")).count():
            return HttpResponse("该班级已存在")
        else:
            models.Class.objects.create(class_name=request.POST.get("class_name"))
            return redirect("/myapp/showClass")

def editClass(request, class_id):
    return HttpResponse("editClass")


def delClass(request, class_id):
    return HttpResponse("delStu")