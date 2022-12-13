from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hai Hemath How are you")
