from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFn(request):
    #print('heloo')
    return HttpResponse('heloo')
def TestFn1(request):
    #print('heloo')
    return render(request,'index.html')