from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def bienvenidos (request):
    return HttpResponse(f'Bienvenidos a Blueberry healthy space. Fecha: {datetime.now().date()}' )

def listar_productos (request): 
    productos = {'producto': ['Arandanos', 'Moras', 'Frutillas']}
    return render(
        request = request, 
        template_name ='compras_1/lista_productos.html',
        context= productos
        )
