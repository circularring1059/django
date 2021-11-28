from django import forms


class ShowForm(forms.Form):
    column = forms.CharField(max_length=20, label='choice')
    column1 = forms.CharField(max_length=20, label='选择')
    sender = forms.EmailField()
