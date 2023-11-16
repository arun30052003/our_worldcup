from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def msd(request):
    return HttpResponse('<center><h1>->MS DHONI<-</h1></center>'
                        '<center><h3>King Of Team & Wicket Keeper')