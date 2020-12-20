from django.db import models
import datetime
# Create your models here.

class mileage(models.Model):
    year=models.IntegerField(default=datetime.date.today().year)
    month=models.IntegerField()
    times=models.FloatField(default=0)
    
class vacation(models.Model):
    vacation_name=models.CharField(max_length=50)
    vacation_left_date=models.IntegerField()
    vacation_date=models.IntegerField()
    doucument_payment=models.IntegerField(default=0)
    vacation_type=models.IntegerField(default=1)
    
class used_vacation(models.Model):
    vacation_name=models.CharField(max_length=50)
    vacation_date=models.IntegerField()
    used_date=models.DateField()
    
class memo(models.Model):
    memotitle=models.CharField(max_length=100)
    memotext=models.TextField(max_length=1000)

class CheckBox(models.Model):
    name=models.CharField(max_length=100)
    weekend=models.IntegerField(default=7)
    find_check=models.BooleanField(default=False)
    checktype=models.IntegerField()
