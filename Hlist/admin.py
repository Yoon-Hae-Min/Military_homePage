from django.contrib import admin
from .models import mileage, vacation, used_vacation, memo, evening, dawn
# Register your models here.


class mileageadmin(admin.ModelAdmin):
    list_display=(
        'id',
        'month',
        'times'
    )
class vacationadmin(admin.ModelAdmin):
    list_display=(
        'id',
        'vacation_name',
        'vacation_left_date',
        'vacation_date',
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
        'memoid',
        'memotitle',
        'memotext'
    )
    
class eveningadmin(admin.ModelAdmin):
    list_display=(
        'evening_name',
        'weekend',
        'find_check'
    )
class dawnadmin(admin.ModelAdmin):
    list_display=(
        'dawn_name',
        'weekend',
        'find_check'
    )
    
    
admin.site.register(mileage,mileageadmin)
admin.site.register(vacation,vacationadmin)
admin.site.register(used_vacation,used_vacationadmin)
admin.site.register(memo,memoadmin)
admin.site.register(evening,eveningadmin)
admin.site.register(dawn,dawnadmin)