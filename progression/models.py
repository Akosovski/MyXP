from django.db import models
from django.contrib.auth.admin import User
from django.utils.timezone import now
# Create your models here.

class Activity(models.Model):
    activity_name = models.CharField(max_length=255)
    activity_xp = models.IntegerField()
    activity_date = models.DateField(default=now)
    activity_summary = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
