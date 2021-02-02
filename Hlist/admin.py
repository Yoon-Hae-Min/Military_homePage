from django.contrib import admin
from .models import mileage, vacation, used_vacation, memo, CheckBox
# Register your models here.


class mileageadmin(admin.ModelAdmin):
    list_display=(
        'id',
        'year',
        'month',
        'times'
    )
class vacationadmin(admin.ModelAdmin):
    list_display=(
        'id',
        'vacation_name',
        'vacation_left_date',
        'vacation_date',
        'doucument_payment',
        'vacation_type',
    )
    fieldsets = [
    (None,{'fields':['vacation_name','vacation_left_date','vacation_date','doucument_payment']}),
    ('0:연가 1:포상 2:위로 3:마일리지', {'fields': ['vacation_type']}),
    ]
class used_vacationadmin(admin.ModelAdmin):
    list_display=(
        'id',
        'vacation_name',
        'vacation_date',
        'used_date'
    )
class memoadmin(admin.ModelAdmin):
    list_display=(
        'memotitle',
        'memotext'
    )
    
class CheckBoxadmin(admin.ModelAdmin):
    list_display=(
        'name',
        'weekend',
        'checktype',
        'find_check'        
    )    
    list_filter=['weekend','checktype']
    fieldsets = [
    (None,{'fields':['name', 'find_check']}),
    ('7:요일전부     8:평일만', {'fields': ['weekend']}),
    ('0:야간     1:조간     2:상시', {'fields': ['checktype']}),
    ]
    
    
admin.site.register(mileage,mileageadmin)
admin.site.register(vacation,vacationadmin)
admin.site.register(used_vacation,used_vacationadmin)
admin.site.register(memo,memoadmin)
admin.site.register(CheckBox,CheckBoxadmin)