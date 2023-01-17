from django.urls import path
from compras_1.views import (
    bienvenidos, listar_productos, listar_clientes,
    listar_comentarios, crear_cliente, buscar_cliente,
    crear_producto, crear_comentario, buscar_producto,
)

urlpatterns = [
    path('bienvenidos/', bienvenidos),
    path('productos/', listar_productos, name="listar_productos"), 
    path('clientes/', listar_clientes, name="listar_clientes"),
    path('comentarios/', listar_comentarios, name="listar_comentarios"),
    path('crear-cliente/', crear_cliente, name="crear_cliente"),
    path('buscar-cliente/', buscar_cliente, name="buscar_cliente"),
    path('crear-producto/', crear_producto, name="crear_producto"),
    path('buscar-producto/', buscar_producto, name="buscar_producto"),
    path('crear-comentario/', crear_comentario, name="crear_comentario"),

]
