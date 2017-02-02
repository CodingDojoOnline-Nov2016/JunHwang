from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
