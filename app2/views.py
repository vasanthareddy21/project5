from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def string1(request):
    return HttpResponse('first string')

def string2(request):
    return HttpResponse('SECOND STRING')
