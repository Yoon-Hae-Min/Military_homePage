from django.contrib import admin
from .models import UploadFileModel
# Register your models here.
class MilUploaderAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'title',
        'file',
        'uploaddate',
        'Ubody',
    )
admin.site.register(UploadFileModel,MilUploaderAdmin)