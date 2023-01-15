from django.urls import path
from compras_1.views import bienvenidos, listar_productos

urlpatterns = [
    path('bienvenidos/', bienvenidos),
    path('productos/', listar_productos)

]