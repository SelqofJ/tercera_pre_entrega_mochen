from django.urls import path
from compras_1.views import bienvenidos, listar_productos, listar_clientes, listar_comentarios, crear_cliente

urlpatterns = [
    path('bienvenidos/', bienvenidos),
    path('productos/', listar_productos, name="listar_productos"), 
    path('clientes/', listar_clientes, name="listar_clientes"),
    path('comentarios/', listar_comentarios, name="listar_comentarios"),
    path('crear-cliente/', crear_cliente, name="crear_cliente"),
]

    
"""
    path('crear-cliente/', crear_cliente, name="crear_cliente"),

  
    path('buscar-cliente/', buscar_cliente, name="buscar_cliente"),
"""
