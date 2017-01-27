from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import Users




# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=45, null=True)
    description = models.TextField(max_length=1000, null=True)
    account = models.ForeignKey(Users, models.DO_NOTHING, related_name ="userstocourses", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
