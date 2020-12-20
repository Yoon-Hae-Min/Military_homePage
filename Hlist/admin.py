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
        'vacation_type',
        'doucument_payment'
    )
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
        'find_check',
        'checktype'
    )    
    
admin.site.register(mileage,mileageadmin)
admin.site.register(vacation,vacationadmin)
admin.site.register(used_vacation,used_vacationadmin)
admin.site.register(memo,memoadmin)
admin.site.register(CheckBox,CheckBoxadmin)