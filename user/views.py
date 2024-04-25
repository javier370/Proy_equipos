from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from user.forms import RegisterForm

def prueba(request):
    msn = 'Hola mi nombre es Javier'

    return render(request, 'prueba.html', {
        'mensaje' : msn,
    })

def registro_user(request):
    title = 'Pagina registro'
    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return redirect('inicio')
        else:
            errors = register_form.errors.as_data()
            error_list = []

            for field, error in errors.items():
                for e in error:
                    if '%(min_length)' in e.message:
                        error_list.append("Esta contraseña es demasiado corta. Debe contener al menos 8 caracteres.")
                    else:
                        error_list.append(f"{e.message}")

            return render(request, 'registro.html', {
                'title' : title,
                'register_form': register_form,
                'errors' : error_list
            })

    return render(request, 'registro.html', {
        'title' : title,
        'register_form': register_form
    })
