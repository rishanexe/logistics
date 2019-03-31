from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Details(models.Model):
    your_name = models.CharField(max_length=10)
    to_name = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=10, null=True)
    good_name = models.CharField(max_length=50, null=True)
    good_type = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    weight = models.IntegerField(default=200)
    address = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=20)
    orderdate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name_plural = "Details"
