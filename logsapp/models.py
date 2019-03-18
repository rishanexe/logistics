from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Details(models.Model):
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    #refid = models.CharField(max_length=8)
    good_type = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    weight = models.IntegerField(default=200)
    location = models.CharField(max_length=20)
    orderdate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name_plural = "Details"
