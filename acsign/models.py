import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Activity(models.Model):
    activity_theme = models.CharField(max_length=200)
    activity_creator = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.activity_theme
    def was_published_recently(self):
        return self.pub_date >= timezone.now()
    datetime.timedelta(days=1)

class Sign(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    sign_name = models.CharField(max_length=200)
    sign_date = models.DateTimeField('date sign')
    def __str__(self):
        return self.sign_name
