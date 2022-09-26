from builtins import map

from django.db import models


# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)

    class Meta:
        db_table = "PRO_User"
