from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros', views.libros, name='libros'),
    path('autores', views.autores, name='autores'),
    path('categorias', views.categorias, name='categorias'),
    path('buscar_libros/', views.buscar_libros, name='buscar_libros'),
    path('obtener_libro/<int:libro_id>/', views.obtener_libro, name='obtener_libro'),  
]