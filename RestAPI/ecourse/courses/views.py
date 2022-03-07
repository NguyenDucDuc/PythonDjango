from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def SayHi(request):
    return HttpResponse("HELLO GUYS !!!")