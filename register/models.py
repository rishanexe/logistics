from django.db import models
from datetime import datetime

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    usertype = models.CharField(max_length=10)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Login"