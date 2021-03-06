from django.contrib import auth
from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto, Marca, Contacto
from .forms import CustomUserCreationForm, ProductoForm, ContactoForm 
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializers, MarcaSerializers

# Create your views here.
class MarcaViewset(viewsets.ModelViewSet):
    queryset=Marca.objects.all()
    serializer_class=MarcaSerializers


class ProductoViewset(viewsets.ModelViewSet):
    queryset= Producto.objects.all()
    serializer_class=ProductoSerializers

    def get_queryset(self):#declaramos para que pueda hacer una consulta directamente en la peticion en caso de recibir una variable
        productos=Producto.objects.all()
        nombre=self.request.GET.get('nombre')

        if nombre:
            productos=productos.filter(nombre__contains=nombre)
        
        return productos


def home(request):
    productos=Producto.objects.all()
    data={
        'productos':productos
    }
    return render(request,'app/home.html',data)

def contacto(request):
    data={
        'formulario' : ContactoForm()
    }
    if request.method=='POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Formulario Enviado'
        else:
            data['formulario']=formulario
            
    return render(request,'app/contacto.html',data)
#@login_required
def galeria(request):
    return render(request,'app/galeria.html')


@permission_required('app.add_producto')
def agregar_producto(request):
    data={
        'form': ProductoForm,
    }
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            try:
                formulario.save()
                messages.success(request,'Producto Agregado con exito')
                #data['mensaje']='Producto Agregado con exito'
                redirect(to='agregar_producto')    
            except:          
        #else:
                data['mensaje']= formulario


    return render(request,'app/producto/agregar.html', data)


@permission_required('app.view_producto')
def listar_productos(request):
    productos=Producto.objects.all()
    page=request.GET.get('page',1)
    try:
        paginator=Paginator(productos,5)
        productos=paginator.page(page)
    except:
        raise Http404

    data={
        'entity':productos,
        'paginator': paginator
    }

    return render(request,'app/producto/listar.html', data)


@permission_required('app.change_producto')
def modificar_producto(request, id):
    producto=get_object_or_404(Producto,id=id)
    data={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto ,files=request.FILES)
        if formulario.is_valid():
            try:
                formulario.save()
                messages.success(request,'modificado con exito')
                #data['mensaje']='Producto editado con exito'
                return redirect(to='listar_productos')
            except:
                data['form']=formulario

    return render(request,'app/producto/modificar.html', data)


@permission_required('app.delete_producto')
def eliminar_producto(request,id):
    producto=get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request,'eliminado con exito')
    return redirect(to="listar_productos")

def registro(request):
    data={
        'form':CustomUserCreationForm
    }
    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                user=authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
                login(request,user)
                messages.success(request,'te has registrado con exito')
                return redirect(to='home')
            except:
                data['form']=formulario

    return render(request, 'registration/registro.html',data)



    