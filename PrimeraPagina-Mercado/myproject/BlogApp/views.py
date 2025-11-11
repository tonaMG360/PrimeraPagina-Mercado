# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm
from django.db.models import Q

# 1. Vista de Inicio (Muestra todos los Posts)
def inicio(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'BlogApp/inicio.html', {'posts': posts})

# 2. Vistas de INSERCIÓN (Ejemplo para Autor, las otras 2 son similares)
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionar después de guardar
            return redirect('inicio')
    else:
        form = AutorForm()
    
    return render(request, 'BlogApp/crear_autor.html', {'form': form, 'modelo': 'Autor'})

# *** Las vistas para Categoria y Post serían similares a crear_autor ***
# Puedes replicar la lógica cambiando el form y la plantilla.

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CategoriaForm()
    return render(request, 'BlogApp/formulario_base.html', {'form': form, 'modelo': 'Categoría'})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'BlogApp/formulario_base.html', {'form': form, 'modelo': 'Post'})


# 3. Vista de BÚSQUEDA
def buscar_post(request):
    form = BusquedaPostForm(request.GET)
    resultados = []
    criterio = ''

    if form.is_valid():
        criterio = form.cleaned_data['criterio_busqueda']
        if criterio:
            # Búsqueda insensible a mayúsculas/minúsculas por el título
            resultados = Post.objects.filter(titulo__icontains=criterio).order_by('titulo')

    return render(request, 'BlogApp/buscar_post.html', {
        'form': form,
        'resultados': resultados,
        'criterio': criterio
    })