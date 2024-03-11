from django.urls import path, include
from .views import *

urlpatterns = [
    # Menú principal
    path('', home, name="home"),
    path('libros/', libros, name="libros"),
    path('autores/', autores, name="autores"),
    path('generos/', generos, name="generos"),

    # Formulario
    path('libro_form/', libroForm, name="libro_form"),

    # Búsqueda
    path('buscar_libros/', buscarLibros, name="buscar_libros"),
    path('encontrar_libros/', encontrarLibros, name="encontrar_libros"),
]