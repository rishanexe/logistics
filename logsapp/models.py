from django.db import models

# Create your models here.
class Details(models.Model):
    customer_name = models.CharField(max_length=200)
    refid = models.CharField(max_length=8)
    good_type = models.CharField(max_length=10)
    packs = models.IntegerField(default=0)
    weight = models.IntegerField(default=200)
    location = models.CharField(max_length=10)

class Login(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    usertype = models.CharField(max_length=10)
