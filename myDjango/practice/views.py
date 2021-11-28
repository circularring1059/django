from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Author, Book
from .form import ShowForm, BookForm


def list_book(request):
    if request.method == "GET":
        try:
            author = Author.objects.get(id=1)
        except (KeyError, author.DoesNotExist):
            error_message = "object DoesNotExist"
            return render(request, "practice/loop.html", locals())
        else:
            print(author)
            print(author.author_book.all)
            return render(request, "practice/loop.html", locals())
    choice = request.POST.get('choice')
    book = get_object_or_404(Book, id=choice)
    print(book)
    return HttpResponse('选择的book is: {}'.format(book.name))


def show_form(request):
    if request.method == "GET":
        test_form = ShowForm()
        return render(request, "practice/show_form.html", locals())
    test_form = ShowForm(request.POST)
    if test_form.is_valid():
        test_form = test_form.cleaned_data
    return HttpResponse("输入的值为:{}\{}\{}".format(test_form.get('column'), test_form.get('column1'),test_form.get('sender')))


def show_book_form(request):
    book_form = BookForm()
    print(book_form)
    return render(request, "practice/show_form.html", locals())