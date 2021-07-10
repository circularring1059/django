from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=8)
    user_passwd = models.CharField(max_length=16)
    user_token = models.CharField(max_length=32, default=None, blank=True, null=True)

    def __str__(self):
        return self.user_name