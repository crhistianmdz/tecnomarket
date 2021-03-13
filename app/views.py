from django.shortcuts import render
from .models import Producto, Marca, Contacto
from .forms import AgregarProdctoForm, ContactoForm 

# Create your views here.
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

def galeria(request):
    return render(request,'app/galeria.html')

def agregar_producto(request):
    data={
        'form': AgregarProdctoForm,
    }
    if request.method=='POST':
        formulario=AgregarProdctoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            try:
                formulario.save()
                data['mensaje']='Producto Agregado con exito'    
            except:          
        #else:
                data['mensaje']= formulario


    return render(request,'app/producto/agregar.html', data)

def listar_productos(request):
    productos=Producto.objects.all()
    data={
        'productos':productos,
    }

    return render(request,'app/producto/listar.html', data)