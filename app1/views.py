from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vasantha(request):
    return HttpResponse('VASANTHA REDDY')

def kavitha(request):
    return HttpResponse('kavitha reddy')
