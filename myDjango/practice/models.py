from django.core.exceptions import ValidationError
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_book',
                               related_query_name="auth_book")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'


class Blog(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=20)

    '''
    默认情况不会验证数据的合法性，完整性，需要显示调用full_clean 进行验证，
    在表单中通过调用is_vaild验证,null 可以看成是一个特殊的字符窜，
    "" 或“xn” 是可以插入数据设置为not null 的字段的，但在调用时“” 时不能验证通过的， “xn” 可以验证通过'''

    def save(self, *args, **kwargs):
        from django.core.exceptions import NON_FIELD_ERRORS
        try:
            self.full_clean()
            super().save(*args, **kwargs)
        except ValidationError as e:
            # print("验证不通过")
            print('验证没通过： %s' % e.message_dict[NON_FIELD_ERRORS])


# 自定义验证器
def is_even_numbers(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(values)s is not an even numbers'),
            params=locals()
        )


class TestVerification(models.Model):
    number = models.IntegerField(validators=[is_even_numbers])

    def save(self, *args, **kwargs):
        try:
            self.full_clean()  # 需要显示调用full_clean  才能进行验证
            super().save(*args, **kwargs)
        except ValidationError as e:
            print("error:{}".format(e))
