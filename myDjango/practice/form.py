from django import forms
from .models import Book


class ShowForm(forms.Form):
    column = forms.CharField(max_length=20, label='choice')
    column1 = forms.CharField(max_length=20, label='选择')
    sender = forms.EmailField()


class BookForm(forms.ModelForm):
    extra_column = forms.CharField(label="ring", max_length=10)

    class Meta:
        model = Book
        fields = ('name',)  #都自动加上label，这里为Name
