from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
from django.urls import reverse
from compras_1.models import Clientes, Productos, Comentarios
from compras_1.forms import ClienteFormulario, ProductoFormulario, ComentarioFormulario

#  INICIO/BIENVENIDA
def bienvenidos (request):
    return HttpResponse(f'Bienvenidos a Blueberry healthy space. Fecha: {datetime.now().date()}' )

def inicio(request):
    return render(
        request=request,
        template_name='compras_1/inicio.html',
    )

# COMENTARIOS
def listar_comentarios (request): 
    comentarios = {
        'comentarios': Comentarios.objects.all()
        }
    return render(
        request=request,
        template_name='compras_1/lista_comentarios.html',
        context=comentarios,       
    )
def crear_comentario(request):
    if request.method == "POST":
        formulario = ComentarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            comentarios = Comentarios(
                comments=data['comments'],)
            comentarios.save()
            creacion_exitosa = reverse('listar_comentarios')
            return redirect(creacion_exitosa)
    else:  # GET
        formulario = ComentarioFormulario()
    return render(
        request=request,
        template_name='compras_1/formulario_comentario.html',
        context={'formulario': formulario},
     )   
#CLIENTES

def listar_clientes(request):
    clientes = {
        'clientes': Clientes.objects.all()
    }
    return render(
        request=request,
        template_name='compras_1/lista_clientes.html',
        context=clientes,
    )

def crear_cliente(request):
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            clientes = Clientes(
                nombre=data['nombre'],
                apellido=data['apellido'], 
                dni=data['dni'],
                email=data['email'],
                fecha_nac=data['fecha_nac'])
            clientes.save()
            creacion_exitosa = reverse('listar_clientes')
            return redirect(creacion_exitosa)
    else:  # GET
        formulario = ClienteFormulario()
    return render(
        request=request,
        template_name='compras_1/formulario_cliente.html',
        context={'formulario': formulario},
     )   

def buscar_cliente(request):
    if request.method == "POST":
        data = request.POST
        clientes = Clientes.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(apellido__exact=data['busqueda'])
        )
        contexto = {
            'clientes': clientes
        }
        return render(
            request=request,
            template_name='compras_1/lista_clientes.html',
            context=contexto,
        )
# PRODUCTO

def listar_productos (request): 
    productos = {
        'productos': Productos.objects.all()
        }
    return render(
        request = request, 
        template_name ='compras_1/lista_productos.html',
        context= productos
    )
def crear_producto(request):
    if request.method == "POST":
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            productos = Productos(
                nombre=data['nombre'],)
            productos.save()
            creacion_exitosa = reverse('listar_productos')
            return redirect(creacion_exitosa)
    else:  
        formulario = ProductoFormulario()
    return render(
        request=request,
        template_name='compras_1/formulario_producto.html',
        context={'formulario': formulario},
     )   

def buscar_producto(request):
    if request.method == "POST":
        data = request.POST
        productos = Productos.objects.filter(
            Q(nombre__contains=data['busqueda']) 
            )
        contexto = {
            'productos': productos
        }
        return render(
            request=request,
            template_name='compras_1/lista_productos.html',
            context=contexto,
        )

