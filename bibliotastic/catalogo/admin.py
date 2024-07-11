from django.contrib import admin
from .models import Autor, Categoria, Libro, NavItem

# Register your models here.

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(NavItem)
