from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pat(request):
    return render(request,'pat.html')

def glenn(request):
    return HttpResponse('<center><h1>->GLENN MAXWELL<-</h1></center>'
                        '<center><h3>All Rounder...</h3></center>')

