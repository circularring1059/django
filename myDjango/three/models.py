from django.db import models

# Create your models here.

class User(models.Model):
    gender = (
        ("male", "男"),
        ("female", "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    passwd = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="女")
    c_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Neta:
        ordering  = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"