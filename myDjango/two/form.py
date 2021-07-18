from django import forms

class StuForm(forms.Form):
     stu_name = forms.CharField(label='学生姓名', max_length=100)