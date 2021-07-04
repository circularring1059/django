from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Class)
admin.site.register((Cat, Person))