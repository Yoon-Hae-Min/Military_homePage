from django.db import models

# Create your models here.

class mileage(models.Model):
    month=models.CharField(max_length=100)
    times=models.FloatField(default=0)
    