from django.db import models
from django.db.models.manager import Manager
# Create your models here.

#自定义manager
class MyManager(Manager):
    def all(self):
    #     return Manager.all(self).filter(class_name__contains="通信")
        print(super().get_queryset())
        return self.get_queryset().filter(class_name__contains="电信")



class Class(models.Model):
    class_name = models.CharField(max_length=8)
    objects = MyManager()

class Student(models.Model):
    stu_name  = models.CharField(max_length=8)
    sc = models.ForeignKey(Class, on_delete=None, default=1)

    def __str__(self):
        return ('name:{},id:{},sc_id:{}'.format(self.stu_name, self.id,  self.sc_id))

class Cat_type(models.Model):
    cat_type_name = models.CharField(max_length=8)

class Cat(models.Model):
    cat_name = models.CharField(max_length=8)
    cat_age = models.IntegerField()
    ct = models.ForeignKey(Cat_type, on_delete=models.SET_NULL, default=1, null=True)   #对应的cat_type 后其值变为None

    def __str__(self):
        return ("name:{} age:{}".format(self.cat_name, self.cat_age))

class Nationality(models.Model):
    na_name = models.CharField(max_length=8)

class Person(models.Model):
    pe_name = models.CharField(max_length=8)
    pn = models.ForeignKey(Nationality, on_delete=models.CASCADE, default=1)   #级联删除
