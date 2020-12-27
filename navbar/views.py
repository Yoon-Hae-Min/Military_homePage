from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth import logout 
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.db.models import Avg, Max, Min, Sum, Q
from .form import UploadFileForm, LoginForm, EtcUploadFileForm
from Hlist.form import *
from .models import UploadFileModel, EtcUploadFileModel
from Hlist.models import *
#import datetime
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

def MilUploadPage_delete(request,pk):
    UploadFileModel.objects.get(pk=pk).delete()
    return redirect('/mil/')

def MilUploadPage_view(request,pk):
    mv=UploadFileModel.objects.get(pk=pk)
    return render(request, 'navbar/milupload_view.html',{'milupload':mv})

def MilUploadPage(request):
    mup=UploadFileModel.objects.all().order_by('-id')
    return render(request, 'navbar/milupload.html',{'milupload':mup})

def edit_file(request,pk):#수정필요
    post=get_object_or_404(UploadFileModel,pk=pk)
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES, instance=post)# instance=post 나머지 기존거로 채우기
        obj=mileage.objects.filter(Q(year=request.POST["year"])&Q(month=request.POST["month"]))
        if (obj):
            obj=mileage.objects.get(Q(year=request.POST["year"])&Q(month=request.POST["month"]))
            obj.times=request.POST["times"]
            obj.save()
        else:
            new_article = mileage.objects.create(
                year=request.POST['year'],
                month=request.POST['month'],
                times=request.POST['times']
                )
        post=form.save(commit=False)
        post.save()
        return redirect('/mil/')
    else:
        form = UploadFileForm(instance=post)
        mt=mileage.objects.last()
    return render(request, "navbar/milupload_upload.html",{'form':form,'miltimes':mt})

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        obj=mileage.objects.filter(Q(year=request.POST["year"])&Q(month=request.POST["month"]))
        if (obj):
            obj=mileage.objects.get(Q(year=request.POST["year"])&Q(month=request.POST["month"]))
            obj.times=request.POST["times"]
            obj.save()
        else:
            new_article = mileage.objects.create(
                year=request.POST['year'],
                month=request.POST['month'],
                times=request.POST['times']
                )
        if (form.is_valid() and request.POST['title'] != ""):
            form.save()
            return redirect('/mil/')
    else:
        form = UploadFileForm()
        mt=mileage.objects.last()
    return render(request, "navbar/milupload_upload.html",{'form':form,'miltimes':mt})

def EtcPage(request):
    etcp=EtcUploadFileModel.objects.all().order_by('-id')
    return render(request, 'navbar/etcupload.html',{'etcupload':etcp})

def Etcupload_file(request):
    if request.method == "POST":
        form = EtcUploadFileForm(request.POST, request.FILES)
        if (form.is_valid() and request.POST['title'] != ""):
            form.save()
            return redirect('/etc/')
    else:
        form = EtcUploadFileForm()
    return render(request, "navbar/etcupload_upload.html",{'form':form})

def Etcedit_file(request,pk):
    post=get_object_or_404(EtcUploadFileModel,pk=pk)
    if request.method == "POST":
        form = EtcUploadFileForm(request.POST, request.FILES, instance=post)# instance=post 나머지 기존거로 채우기
        post=form.save(commit=False)
        post.save()
        return redirect('/etc/')
    else:
        form = EtcUploadFileForm(instance=post)
    return render(request, "navbar/etcupload_upload.html",{'form':form})

def EtcUploadPage_delete(request,pk):
    EtcUploadFileModel.objects.get(pk=pk).delete()
    return redirect('/etc/')

def EtcUploadPage_view(request,pk):
    eu=EtcUploadFileModel.objects.get(pk=pk)
    return render(request, 'navbar/etcupload_view.html',{'etcupload':eu})
