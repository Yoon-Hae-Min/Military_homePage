from django.contrib import admin
from .models import mileage
# Register your models here.

@admin.register(mileage)
class mileageadmin(admin.ModelAdmin):
    list_display=(
        'id',
        'month',
        'times'
    )
