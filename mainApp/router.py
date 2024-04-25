from django.urls import path
import mainApp.views

urlpatterns = [
    path('', mainApp.views.inicio, name='inicio'),
]