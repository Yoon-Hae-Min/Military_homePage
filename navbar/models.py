from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from ckeditor_uploader.fields import RichTextUploadingField
import os
# Create your models here.
class OverWriteStorage(FileSystemStorage):
    def get_available_name(self,name,max_length=None):
        if(self.exists(name)):
            os.remove(os.path.join(settings.MEDIA_ROOT,name))
        return name

class EtcUploadFileModel(models.Model):
    title = models.CharField(max_length=64, null=True, verbose_name='제목')
    file = models.FileField(storage=OverWriteStorage())
    uploaddate=models.DateField(auto_now_add=True)
    Ubody =RichTextUploadingField(blank=True,null=True)

class UploadFileModel(models.Model):
    title = models.CharField(max_length=64, null=True, verbose_name='제목')
    file = models.FileField(storage=OverWriteStorage())
    uploaddate=models.DateField(auto_now_add=True)
    Ubody =RichTextUploadingField(blank=True,null=True)
    

