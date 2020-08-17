from django.shortcuts import render
from .models import mileage
def main(request):
    mil=mileage.objects.all()
    return render(request,'Hlist/main.html',{'mileage':mil})


# Create your views here.
