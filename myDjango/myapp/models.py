from django.db import models

# Create your models here.



class Class(models.Model):
    class_name = models.CharField(max_length=8)

class Student(models.Model):
    stu_name  = models.CharField(max_length=8)
    sc = models.ForeignKey(Class, on_delete=None, default=1)