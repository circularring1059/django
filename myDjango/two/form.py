from django import forms
from .models import *

class StuForm(forms.Form):
     stu_name = forms.CharField(label='学生姓名', max_length=100)


