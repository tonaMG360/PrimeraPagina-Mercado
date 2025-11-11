from django.db import models

# Create your models here.
from django.db import models

# Modelo 1: Autor del Post
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

# Modelo 2: Categoría para organizar los Posts
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo 3: El Post o Artículo principal
class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    subtitulo = models.CharField(max_length=250, blank=True, null=True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    # Claves Foráneas
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo