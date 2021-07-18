from django.db import models

# Create your models here.

class Car(models.Model):
    #vebose_name  admin 后台字段有关
    car_name = models.CharField(max_length=8, verbose_name="carName",)

    def __str__(self):
        return (self.car_name)

    class Meta:
        db_table = "car"  #db_table 数据库表名， 默认为模型名app_模型名小写  two_car
        verbose_name = "车"
        verbose_name_plural = verbose_name
        ordering = ["-id", "car_name"]    #默认排序，当然可以是使用orm 排序




class User(models.Model):
    stu_name = models.CharField(max_length=32,)