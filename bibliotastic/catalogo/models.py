from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    anio_publicacion = models.IntegerField()
    descripcion_breve = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Nav(models.Model):
    id_nav = models.AutoField(db_column='idNav', primary_key=True)
    nombre_nav = models.CharField(max_length=20, blank=False, null=False)
    url_nav = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_nav)

    class Meta:
        db_table = 'Navs'