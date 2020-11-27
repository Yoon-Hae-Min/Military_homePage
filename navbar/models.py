from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class EtcUploadFileModel(models.Model):
    title = models.CharField(max_length=64, null=True, verbose_name='제목')
    file = models.FileField()
    uploaddate=models.DateField(auto_now_add=True)
    Ubody =RichTextUploadingField(blank=True,null=True)

class UploadFileModel(models.Model):
    title = models.CharField(max_length=64, null=True, verbose_name='제목')
    file = models.FileField()
    uploaddate=models.DateField(auto_now_add=True)
    Ubody =RichTextUploadingField(blank=True,null=True)