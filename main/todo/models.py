from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    date = models.DateTimeField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    notification = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date'] # will order tasks depending on if it is complete or not

