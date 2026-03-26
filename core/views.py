from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Bienvenido al Proyecto Django</h1><p>Rama: dev</p>')
