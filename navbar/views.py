from django.shortcuts import render,redirect
from django.contrib.auth import logout 
from django.contrib import auth
from django.contrib.auth import login, authenticate
from .form import UploadFileForm, LoginForm
from Hlist.form import *
from .models import UploadFileModel
import datetime
# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        # 폼 객체, 폼 클래스를 만들 때 괄호에 POST 데이터를 담아준다.
        # POST 안에 있는 데이터가 form 변수에 들어간다.
        u=authenticate(username=username,password=password)

        if u is not None:
            auth.login(request,u)
            return redirect('/')
    else:
        form = LoginForm()
        # 빈 클래스 변수를 만든다.
    return render(request, 'navbar/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def MilUploadPage_view(request,pk):
    mv=UploadFileModel.objects.get(pk=pk)
    return render(request, 'navbar/milupload_view.html',{'milupload':mv})

def MilUploadPage(request):
    mup=UploadFileModel.objects.all()
    return render(request, 'navbar/milupload.html',{'milupload':mup})

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if (form.is_valid() and request.POST['title'] != ""):
            form.save()
            return redirect('/')
    else:
        form = UploadFileForm()
    return render(request, "navbar/milupload_create.html",{'form':form})