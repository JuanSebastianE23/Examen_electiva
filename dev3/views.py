from django.shortcuts import render

def hoja_vida(request):
    context = {
        'nombre': 'Desarrollador 3',
        'profesion': 'Desarrollador Frontend',
        'email': 'dev3@example.com',
        'telefono': '+57 302 345 6789',
        'perfil': 'Experto en interfaces de usuario y experiencia del usuario.',
        'formacion': [
            {'titulo': 'Diseño y Desarrollo Web', 'institucion': 'Universidad DEF', 'año': '2020-2024'},
        ],
        'repositorios': [
            {'nombre': 'Portfolio React', 'url': 'https://github.com/dev3/portfolio-react'},
        ]
    }
    return render(request, 'dev3/hoja_vida.html', context)
