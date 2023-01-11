from django.http import HttpResponse
from django.shortcuts import render

def hola_mundo(request):
    return HttpResponse("hola mundo")