from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=8)
    user_passwd = models.CharField(max_length=16)
    user_token = models.CharField(max_length=32, default=None, blank=True, null=True)

    def __str__(self):
        return self.user_name

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        # extral code
        """
        book = Book.create("liujiangblog.com")   
        book.save()        # 只有调用save后才能保存到数据库
        """
        return book


class BookManager(models.Manager):   # 继承默认的管理器
    def create_book(self, title):
        book = self.create(title=title)
        # 将你的个人代码放在这里
        print('测试一下是否工作正常')
        return book

class Book(models.Model):
    title = models.CharField(max_length=100)

    objects = BookManager()   # 赋值objects
    """
    book = Book.objects.create_book("*********")   #改为使用create_book方法创建对象
    """