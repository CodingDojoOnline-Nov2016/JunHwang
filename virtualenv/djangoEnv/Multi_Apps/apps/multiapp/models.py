from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import Users
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=45)
    blog = models.TextField(max_length=1000)
    blog_creator = models.ForeignKey(Users)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
