from django.contrib import admin
from .models import UploadFileModel, EtcUploadFileModel
# Register your models here.
class MilUploaderAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'title',
        'file',
        'uploaddate',
        'Ubody',
    )
class EtcUploaderAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'title',
        'file',
        'uploaddate',
        'Ubody',
    )
admin.site.register(UploadFileModel,MilUploaderAdmin)
admin.site.register(EtcUploadFileModel,EtcUploaderAdmin)