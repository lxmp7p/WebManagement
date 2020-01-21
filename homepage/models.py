from django.db import models


# Create your models here.

class Equipment(models.Model):
    equip_name = models.CharField(max_length=150)
    serial_id = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
