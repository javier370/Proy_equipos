from django.urls import path
import user.views

urlpatterns = [
    path('prueba/', user.views.prueba, name='pagina-prueba'),
    path('registro/', user.views.registro_user, name='registro'),
]