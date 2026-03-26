from django.shortcuts import render

def hoja_vida(request):
    context = {
        'nombre': 'Maria Alejandra Montilla Díaz',
        'profesion': 'Estudiante de Ingeniería de Software',
        'email': 'alejadiiaz27@gmail.com',
        'telefono': '+57 316 237 6930',
        'perfil': 'Estudiante de Ingeniería de Software apasionada por el desarrollo web y la creación de soluciones tecnológicas innovadoras. Con experiencia en proyectos académicos y personales que abarcan desde el desarrollo frontend hasta la arquitectura de software, busco constantemente aprender nuevas tecnologías y aplicarlas en proyectos con impacto real.',
        'formacion':
            {
                'titulo': 'Ingeniería de Software',
                'institucion': 'Universidad Cooperativa de Colombia',
                'año': '2022 - Actualidad',
            },
    }
    return render(request, 'dev3/hoja_vida.html', context)