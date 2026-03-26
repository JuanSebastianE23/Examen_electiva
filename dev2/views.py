from django.shortcuts import render

def hoja_vida(request):
    context = {
        'nombre': 'Desarrollador 2',
        'profesion': 'Desarrollador Backend',
        'email': 'dev2@example.com',
        'telefono': '+57 301 234 5678',
        'perfil': 'Especialista en arquitectura de software y bases de datos.',
        'formacion': [
            {'titulo': 'Ingeniería de Software', 'institucion': 'Universidad ABC', 'año': '2019-2023'},
        ],
        'repositorios': [
            {'nombre': 'API REST', 'url': 'https://github.com/dev2/api-rest'},
        ]
    }
    return render(request, 'dev2/hoja_vida.html', context)
