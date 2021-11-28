from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Author, Book


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
    choice= request.POST.get('choice')
    book = get_object_or_404(Book,id=choice)
    print(book)
    return HttpResponse('选择的book is: {}'.format(book.name))
