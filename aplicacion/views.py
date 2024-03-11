from django.shortcuts import render

from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def autores(request):
    contexto = {'autores': Autor.objects.all()}
    return render(request, "aplicacion/autores.html", contexto)

def generos(request):
    contexto = {'generos': Genero.objects.all()}
    return render(request, "aplicacion/generos.html", contexto)

def libros(request):
    contexto = {'libros': Libro.objects.all()}
    return render(request, "aplicacion/libros.html", contexto)

# Formularios

def libroForm(request):
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            libro_titulo = miForm.cleaned_data.get("titulo")
            libro_autor = miForm.cleaned_data.get("autor")
            libro_genero = miForm.cleaned_data.get("genero")
            libro_ano_publicacion = miForm.cleaned_data.get("ano_publicacion")
            libro_isbn = miForm.cleaned_data.get("isbn")
            libro = Libro(titulo=libro_titulo, 
                          autor=libro_autor, 
                          genero=libro_genero, 
                          ano_publicacion=libro_ano_publicacion, 
                          isbn=libro_isbn)
            libro.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = LibroForm()
    return render(request, "aplicacion/libroForm.html", {"form": miForm})

# Búsqueda

def buscarLibros(request):
    return render(request, "aplicacion/buscar.html")

def encontrarLibros(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        libros = Libro.objects.filter(titulo__icontains=patron)
        contexto = {"libros": libros}
        return render(request, "aplicacion/libros.html", contexto)
    contexto = {'libros': Libro.objects.all()}
    return render(request, "aplicacion/libros.html", contexto)