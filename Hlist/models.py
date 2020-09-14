from django.db import models

# Create your models here.

class mileage(models.Model):
    month=models.CharField(max_length=100)
    times=models.FloatField(default=0)
    
class vacation(models.Model):
    vacation_name=models.CharField(max_length=50)
    vacation_left_date=models.IntegerField()
    vacation_date=models.IntegerField()
    doucument_payment=models.IntegerField(default=0)
    
class used_vacation(models.Model):
    vacation_name=models.CharField(max_length=50)
    vacation_date=models.IntegerField()
    used_date=models.DateField()
    
class memo(models.Model):
    memoid=models.IntegerField(default=1)
    memotitle=models.CharField(max_length=100)
    memotext=models.TextField(max_length=1000)

class evening(models.Model):
    evening_name=models.CharField(max_length=100)
    weekend=models.IntegerField(default=7)
    find_check=models.BooleanField(default=False)
    
class dawn(models.Model):
    dawn_name=models.CharField(max_length=100)
    weekend=models.IntegerField(default=7)
    find_check=models.BooleanField(default=False)
