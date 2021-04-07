from django.db import models
from django.db.models.fields import DateTimeField
# Create your models here.

class Note(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=160, blank = True, default = 'untitled')
    body = models.TextField()

    class Meta:
        ordering = ['date_updated']

