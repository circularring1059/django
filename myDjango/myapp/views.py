"""
on_delete=None, # 删除关联表中的数据时,当前表与其关联的field的行为
on_delete=models.CASCADE, # 删除关联数据,与之关联也删除
on_delete=models.DO_NOTHING, # 删除关联数据,什么也不做
on_delete=models.PROTECT, # 删除关联数据,引发错误ProtectedError
# models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
on_delete=models.SET_NULL, # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
# models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
on_delete=models.SET, # 删除关联数据,
"""
import pymysql
from  django.db import connection
from django.shortcuts import render, redirect
from django.urls import path, re_path
from django.http import HttpResponse, Http404
from myapp import models
from django.views import View

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
        class_list = models.Class.objects.all()
    #     print(locals())
    #     for i in  class_list:
    #         print(i.id, i.class_name)
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
    print(class_list.query)  #query  orm 转成 sql
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
    if request.method == "GET":
        class_name = models.Class.objects.all().values("class_name").get(id=class_id)
        return render(request, "editClass.html", locals())
    else:
        models.Class.objects.all().filter(id=class_id).update(class_name=request.POST.get("class_name"))
        return redirect("/myapp/showClass")

def delClass(request, class_id):
    models.Class.objects.all().filter(id=class_id).delete()
    return redirect("/myapp/showClass")


def getPerson(request):
    # orm 执行原生sql   ***这里必须包含主键***
    person_list = models.Person.objects.raw("select id, pe_name from myapp_person")
    for person in person_list:
        print(person.id, person.pe_name)
    return HttpResponse("getPerson")


def getCat(request):
    cursor = connection.cursor()
    #可以不用主键
    cursor.execute('select * from myapp_cat')
    cat_list = cursor.fetchall()
    for cat in cat_list:
        print(cat)
    return HttpResponse("getCat")

#
class EditCat(View):
    def get(self, request):
        return HttpResponse("get method")

    def post(self, request):
        return HttpResponse("post methodd")