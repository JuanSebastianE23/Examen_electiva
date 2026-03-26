from django.shortcuts import render

def hoja_vida(request):
    context = {
        'nombre': 'Desarrollador 1',
        'profesion': 'Desarrollador Full Stack',
        'email': 'dev1@example.com',
        'telefono': '+57 300 123 4567',
        'perfil': 'Desarrollador apasionado por crear soluciones web innovadoras.',
        'formacion': [
            {'titulo': 'Ingeniería de Sistemas', 'institucion': 'Universidad XYZ', 'año': '2020-2024'},
        ],
        'repositorios': [
            {'nombre': 'Proyecto Django', 'url': 'https://github.com/dev1/proyecto-django'},
        ]
    }
    return render(request, 'dev1/hoja_vida.html', context)
