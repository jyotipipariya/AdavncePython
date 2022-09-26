
from builtins import map

from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    mobileNumber = models.IntegerField
    class Meta:
        db_table = "SOS_User"


