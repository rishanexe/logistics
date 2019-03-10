from django.db import models
from datetime import datetime

# Create your models here.
class Details(models.Model):
    customer_name = models.CharField(max_length=200)
    refid = models.CharField(max_length=8)
    good_type = models.CharField(max_length=10)
    packs = models.IntegerField(default=0)
    weight = models.IntegerField(default=200)
    location = models.CharField(max_length=10)
    orderdate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.refid

    class Meta:
        verbose_name_plural = "Details"
