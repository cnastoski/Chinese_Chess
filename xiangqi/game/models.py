from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=16)


