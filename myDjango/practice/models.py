from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='author_book', related_query_name="auth_book")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'

#
# class FileFile(models.Model):
#     file_object = models.FileField(upload_to='/uploads/%Y/%m%d')
#
