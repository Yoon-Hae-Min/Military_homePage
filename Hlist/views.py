from django.shortcuts import render,redirect
from .models import mileage,vacation,used_vacation,memo
from django.core.exceptions import ObjectDoesNotExist
def main(request):
    mil=mileage.objects.all()
    vac=vacation.objects.all()
    uvac=used_vacation.objects.all()
    memos=memo.objects.all()
    return render(request,'Hlist/main.html',{'mileage':mil, 'vacation':vac, 'used_vacation':uvac, 'memo':memos})


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
