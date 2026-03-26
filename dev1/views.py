from django.shortcuts import render

def hoja_vida(request):
    """Vista para la hoja de vida de Marlon Andrade - Dev 1"""
    return render(request, 'dev1/hoja_vida.html')
