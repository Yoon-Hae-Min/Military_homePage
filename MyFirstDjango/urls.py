"""MyFirstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from Hlist.views import *
from navbar.views import *

app_name = 'Mil' 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('post/', postmemo),
    path('delete/<pk>', memodelete),
    path('edit/<pk>',memoedit),
    path('eveningCheckBox/', SaveEveningCheckBox),
    path('dawnCheckBox/', SaveDawnCheckBox),
    path('checkboxrelease/', AllCheckBoxRelease, name="AllCheckBoxRelease"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('mil/', MilUploadPage, name="mileage"),
    path('mil/<pk>',MilUploadPage_view,name="view"),
    path('milupload/',upload_file,name="milupload"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('mil/<pk>/delete',MilUploadPage_delete,name="delete"),
    path('mil/<pk>/edit',edit_file,name="edit"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

