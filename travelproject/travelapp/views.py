from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import members
# Create your views here.


def index(request):
   obj=place.objects.all()
   memb=members.objects.all()
   return render(request,"index.html",{'result':obj,'output':memb})

