from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # La ruta vacía '' significa la página principal
]