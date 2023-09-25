from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def inicio(request):
    msn = 'Bienvenido a mi web'

    return render(request, 'inicio.html', {
        'mensaje' : msn,
    })
