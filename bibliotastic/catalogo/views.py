from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Libro, Autor, Categoria, Nav
from django.http import JsonResponse



# Create your views here.

def index(request):
    navs = Nav.objects.all()
    context = {'navs':navs}
    return render(request, 'catalogo/index.html', context)

def libros(request):
    navs = Nav.objects.all()
    libros = Libro.objects.all()
    context = {'navs':navs, 'libros':libros}
    return render(request, 'catalogo/libros.html', context)

def autores(request):
    navs = Nav.objects.all()
    autores = Autor.objects.all()
    context = {'navs':navs, 'autores':autores}
    return render(request, 'catalogo/autores.html', context)

def categorias(request):
    navs = Nav.objects.all()
    categorias = Categoria.objects.all()
    context = {'navs':navs, 'categorias':categorias}
    
    return render(request, 'catalogo/categorias.html', context)

def buscar_libros(request):
    if request.method == 'GET' and 'titulo' in request.GET:
        titulo_libro = request.GET.get('titulo', '')
        libros = Libro.objects.filter(titulo__icontains=titulo_libro)

      
        libros_json = []
        for libro in libros:
            libros_json.append({
                'titulo': libro.titulo,
                'anio_publicacion': libro.anio_publicacion,
                'descripcion_breve': libro.descripcion_breve
            })

       
        return JsonResponse({'libros': libros_json})

    
    return JsonResponse({'libros': []})





def obtener_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    data = {
        'titulo': libro.titulo,
        'anio_publicacion': libro.anio_publicacion,
        'descripcion_breve': libro.descripcion_breve,
        # Agregar más campos según sea necesario
    }
    return JsonResponse(data)



