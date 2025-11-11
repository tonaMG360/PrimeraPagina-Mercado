# BlogApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs principales
    path('', views.inicio, name='inicio'),
    
    # URLs de Inserción (CRUD - Create)
    path('autor/crear/', views.crear_autor, name='crear_autor'),
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'),
    path('post/crear/', views.crear_post, name='crear_post'),
    
    # URL de Búsqueda
    path('post/buscar/', views.buscar_post, name='buscar_post'),
]