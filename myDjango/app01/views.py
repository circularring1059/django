from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

#获取班级
def  getClass(request):
    import pymysql
    connect = pymysql.connect(host="192.168.10.173", port=3309, user="root", passwd="ring", db="ring", charset="utf8")
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select class_name, id from class")
    class_list = cursor.fetchall()
    cursor.close()
    connect.close()
    # print(class_list, "locals:", locals())
    return render(request, "getClass.html", locals())

def  addClass(request):
    if request.method == "GET":
        # import pymysql
        # connect = pymysql.connect(host="192.168.10.173", port=3309, user="root", passwd="ring", db="ring", charset="utf8")
        # cursor = connect.cursor(pymysql.cursors.DictCursor)
        # print(request.POST())
        return render(request, "addClass.html")
    else:
        postData = request.POST
        print(postData)
        # return HttpResponse("addClass")
        name = request.POST.get('name')
        id = request.POST.get("classId")
        sql = "insert into class(name, id) values('{}',{});".format(name, id)
        # sql = 'insert into class(name, id) values("通信五班", 11)'
        # return HttpResponse("hello")
        print(sql)
        if id == None or name == None:
            raise("keyErr")
        else:
            import pymysql
            connect = pymysql.connect(host="192.168.10.173", port=3309, user="root", passwd="ring", db="ring", charset="utf8")
            cursor = connect.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            connect.commit()
            cursor.close()
            connect.close()
            return redirect("/getClass")


def  delClass(request):
    print(request.GET.get("id"))
    # return HttpResponse("删除成功")
    sql = "delete from class where id = '{}';".format(request.GET.get("id"))
    print(sql)
    import pymysql
    connect = pymysql.connect(host="192.168.10.173", port=3309, user="root", passwd="ring", db="ring", charset="utf8")
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()
    return redirect("/getClass")

def  editClass(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    # print(id, name)
    if request.method == "GET":
        return render(request, "editClass.html", locals())
    else:
        name  = request.POST.get("name")
        id = request.POST.get('id')
        import pymysql
        connect = pymysql.connect(host="192.168.10.173", port=3309, user="root", passwd="ring", db="ring", charset="utf8")
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        cursor.execute("update class set name='{}' where id = {}".format(name, id))
        connect.commit()
        cursor.close()
        connect.close()
        return redirect("/getClass/")

def  getStu(request):
    import pymysql
    connect = pymysql.connect(host="192.168.10.173", port=3309, user="root", passwd="ring", db="ring", charset="utf8")
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    # cursor.execute("select stu_name from student")
    cursor.execute("select student.id, stu_name, class_name from student, class where student.class_id = class.id;")
    stu_list =  cursor.fetchall()
    cursor.close()
    connect.close()
    # return HttpResponse(stu_list)
    print(stu_list)
    return render(request, "getStu.html", locals())

def delStu(request):
    # return HttpResponse("删除成功")
    data = request.GET
    import pymysql
    connect = pymysql.connect(host="192.168.10.173", port=3309, user="root", passwd="ring", db="ring", charset="utf8")
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    cursor.execute("delete from student where id={}".format(request.GET.get("id")))
    connect.commit()
    cursor.close()
    connect.close()
    return redirect("/getStu")

def addStu(request):
    # return HttpResponse("添加成功")
    if request.method == "GET":
        return render(request, 'addStu.html')
    else:
        # import pymysql
        # connect = pymysql.connect(host="192.168.10.173", port=3309, user="root", passwd="ring", db="ring", charset="utf8")
        # cursor = connect.cursor()
        # cursor.execute("insert into sutdent(stu_name, class_id) values('{}', {})".format(request.POST.get(stu_name),request.POST.get("class_name")))
        # connect.commit()
        # cursor.close()
        # connect.close()
        # return redirect("/getStu")
        return HttpResponse(request.POST.get("stu_name"))