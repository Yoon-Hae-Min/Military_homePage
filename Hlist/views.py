from django.shortcuts import render,redirect
from .models import mileage,vacation,used_vacation,memo,CheckBox
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Max, Min, Sum, Q
from django.contrib.auth.forms import UserCreationForm
import datetime
from .form import PostMemoClass



def main(request):
    dt = datetime.datetime.now()
    if(dt.weekday()<5):
        today=8
    else:
        today=dt.weekday()
    mil=mileage.objects.all()
    milsum=mileage.objects.all().aggregate(Sum('times'))
    vac=vacation.objects.all()
    uvac=used_vacation.objects.all()
    memos=memo.objects.all()
    ev=CheckBox.objects.filter(Q(weekend=7) | Q( weekend=dt.weekday()) |Q(weekend=today))
    return render(request,'Hlist/main.html',{'mileage':mil, 'vacation':vac, 'used_vacation':uvac, 'memo':memos,'CheckBox':ev, 'mileagesum':milsum})

    
def postmemo(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        if (request.POST['memotext'] != "") :
            new_article = memo.objects.create(
                memotitle=request.POST['memotitle'],
                memotext=request.POST['memotext']
                )
            return redirect('/')
    form=PostMemoClass()
    return render(request, 'Hlist/post.html',{'form':form})

def memodelete(request,pk):
    memo.objects.get(pk=pk).delete()
    return redirect('/')

def memoedit(request, pk):
    memoCopy=memo.objects.get(pk=pk)
    memotitle=memoCopy.memotitle
    memotext=memoCopy.memotext
    if request.method == "POST":
        memoCopy.memotitle=request.POST['memotitle']
        memoCopy.memotext=request.POST['memotext']
        memoCopy.save()
        return redirect('/')
    return render(request, 'Hlist/edit.html',{'memotitle':memotitle, 'memotext':memotext})
        
    
def SaveCheckBox(request):
    if request.method == 'POST':
        check_values=request.POST.getlist('chk[]')
        ev=CheckBox.objects.all()
        for i in ev:
            i.find_check=False
            i.save()
        for x in check_values:
            getId=CheckBox.objects.get(id=x)
            getId.find_check=True
            getId.save()
    return redirect('/')

def AllCheckBoxRelease(request):
    ev=CheckBox.objects.all()
    for ev in ev:
        ev.find_check=False
        ev.save()
    return redirect('/')
        