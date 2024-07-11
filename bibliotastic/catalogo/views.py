from django.shortcuts import render
from .models import Libro, Autor, Categoria

# Create your views here.

def index(request):
    return render(request, 'catalogo/index.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/libros.html', {'libros': libros})

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/autores.html', {'autores': autores})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/categorias.html', {'categorias': categorias})
