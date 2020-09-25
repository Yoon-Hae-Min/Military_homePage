from django.shortcuts import render,redirect
from .models import mileage,vacation,used_vacation,memo,evening,dawn
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Max, Min, Sum, Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout 
from django.contrib import auth
from .form import LoginForm
import datetime
from django.contrib.auth import login, authenticate


def main(request):
    dt = datetime.datetime.now()
    mil=mileage.objects.all()
    milsum=mileage.objects.all().aggregate(Sum('times'))
    vac=vacation.objects.all()
    uvac=used_vacation.objects.all()
    memos=memo.objects.all()
    ev=evening.objects.filter(Q(weekend=7) | Q( weekend=dt.weekday()))
    da=dawn.objects.filter(Q(weekend=7) | Q( weekend=dt.weekday()))
    return render(request,'Hlist/main.html',{'mileage':mil, 'vacation':vac, 'used_vacation':uvac, 'memo':memos,'evening':ev,'dawn':da, 'mileagesum':milsum})


def postmemo(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        if (request.POST['memoid'] != "==선택==" and request.POST['memotext'] != "") :
            objects=memo.objects.filter(memoid=request.POST['memoid']).first() #필터로 검색 해서 없으면 None반환
            if(objects!=None):
                delete_object=memo.objects.get(memoid=request.POST['memoid'])
                delete_object.delete()
            new_article = memo.objects.create(
                memoid=request.POST['memoid'],
                memotitle=request.POST['memotitle'],
                memotext=request.POST['memotext']
                )
            return redirect('/')

        # 새글 등록 끝
    return render(request, 'Hlist/post.html')

def postdelete(request,pk):
    objects=memo.objects.get(memoid=pk)
    objects.delete()
    return redirect('/')
        
    
def SaveEveningCheckBox(request):
    if request.method == 'POST':
        check_values=request.POST.getlist('chk[]')
        ev=evening.objects.all()
        for i in ev:
            i.find_check=False
            i.save()
        for x in check_values:
            getId=evening.objects.get(id=x)
            getId.find_check=True
            getId.save()
    
    return redirect('/')

def SaveDawnCheckBox(request):
    if request.method == 'POST':
        check_values=request.POST.getlist('chkD[]')
        da=dawn.objects.all()
        for i in da:
            i.find_check=False
            i.save()
        for x in check_values:
            getId=dawn.objects.get(id=x)
            getId.find_check=True
            getId.save()
    return redirect('/')

def AllCheckBoxRelease(request):
    ev=evening.objects.all()
    da=dawn.objects.all()
    for ev in ev:
        ev.find_check=False
        ev.save()
    for da in da:
        da.find_check=False
        da.save()
    return redirect('/')
        
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
    return render(request, 'Hlist/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')