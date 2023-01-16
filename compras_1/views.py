from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
from django.urls import reverse
from compras_1.models import  Clientes, Productos, Estado_producto, Comentarios
from compras_1.forms import FormularioCliente

def bienvenidos (request):
    return HttpResponse(f'Bienvenidos a Blueberry healthy space. Fecha: {datetime.now().date()}' )

def inicio(request):
    return render(
        request=request,
        template_name='compras_1/inicio.html',
    )

def listar_productos (request): 
    productos = {'producto': ['Arandanos', 'Moras', 'Frutillas']}
    return render(
        request = request, 
        template_name ='compras_1/lista_productos.html',
        context= productos
    )

def listar_clientes(request):
    clientes = {
        'compras_1': Clientes.objects.all()
    }
    return render(
        request=request,
        template_name='compras_1/lista_clientes.html',
        context=clientes,
    )


def crear_cliente(request):
    if request.method == "POST":
        formulario = FormularioCliente(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Clientes(nombre=data['nombre'], apellido=data['apellido'])
            curso.save()
            url_exitosa = reverse('listar_clientes')
            return redirect(url_exitosa)
    else:  # GET
        formulario = FormularioCliente()
    return render(
        request=request,
        template_name='compras_1/formulario_cliente.html',
        context={'formulario': formulario},
     )   
"""
def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )
"""