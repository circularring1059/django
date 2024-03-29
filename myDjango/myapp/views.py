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
import pymysql, uuid
from  django.db import connection
from django.shortcuts import render, redirect
from django.urls import path, re_path
from django.http import HttpResponse, Http404
from myapp import models
from django.views import View
from django.db.models import Max, Min, Sum
from django.db.models import Q, F

def index(request):
    return render(request, "myapp_index.html")

def showStu(request):
    current_page = request.GET.get("page",1)  #开始默认为第一页
    stu_list = models.Student.objects.all()
    # stu_list = models.Student.objects.all().filter(id__gt=100)  # __gt   大于100
    # stu_list = models.Student.objects.all().filter(id__gte=100)  # __gt   大于等于100
    # stu_list = models.Student.objects.all().filter(sc_id__lt=-1)  # __lt   小于-1
    # stu_list = models.Student.objects.all().filter(id__lte=0)  # __gt   小于等于等于0
    # stu_list = models.Student.objects.all().filter(id__in=[2, 66, 57])  # in   2, 66, 57   == for  i in string:
    # stu_list = models.Student.objects.all().filter(id__range=(66,100))  # range    范围
    # stu_list = models.Student.objects.all().filter(stu_name__startswith="葡")  # startwith
    # stu_list = models.Student.objects.all().filter(stu_name__endswith="子")  # endwith
    # stu_list = models.Student.objects.all().filter(stu_name__contains="桃")  # endwith
    # stu_list = models.Student.objects.all().filter(stu_name__exact="子")  #   精确查找   加i 不 区分大小写
    # stu_list = models.Student.objects.all().exclude(id=57)  #  排除id  等于57
    #分页
    from django.core.paginator import Page, PageNotAnInteger, Paginator, EmptyPage, InvalidPage
    #实例化page 对象
    paginator = Paginator(stu_list, 2)
    #page页码对象

    try:
        page = paginator.page(current_page)  #这个current_page  type 为str时可以自定转为int  前提是能转为int
    except EmptyPage as e:
        page = paginator.page((1))
    except PageNotAnInteger as e:
        page = paginator.page(1)
    print(stu_list)
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
    print(class_id)
    models.Class.objects.all().filter(id=class_id).delete()
    return redirect("/myapp/showClass")


def getPerson(request):
    # orm 执行原生sql   ***这里必须包含主键***
    person_list = models.Person.objects.raw("select id, pe_name from myapp_person")
    for person in person_list:
        print(person.id, person.pe_name)
    return HttpResponse("getPerson")


def getCat(request):
    # cursor = connection.cursor()
    # #可以不用主键
    # cursor.execute('select * from myapp_cat')
    # cat_list = cursor.fetchall()
    # for cat in cat_list:
    #     print(cat)
    # models.Cat.objects.all().update(cat_age= F("cat_age") + 1)   #  F 元数据操作
    # cat_list = models.Cat.objects.all()
    # cat_one = models.Cat.objects.all().filter(cat_name="二猫").first()
    # print(cat_one.cat_age)
    # cat_one.cat_age += 1
    # cat_one.save()
    # print(cat_one)
    # cat_one = models.Cat.objects.all().filter(cat_age=id)
    return HttpResponse("getCat")

#cbv
class EditCat(View):
    def get(self, request):
        return HttpResponse("get method")

    def post(self, request):
        return HttpResponse("post methodd")