from django.db import models
from django import forms


# Create your models here.

class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    equip_name = models.CharField(max_length=150)
    serial_id = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    floor = models.IntegerField()
    building = models.CharField(max_length=50)
