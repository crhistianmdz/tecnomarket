from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('producto', views.ProductoViewset)
router.register('marca',views.MarcaViewset)

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/',views.contacto,name='contacto'),
    path('galeria/',views.galeria,name='galeria'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('productos/',views.listar_productos,name='listar_productos'),
    path('modificar-producto/<id>',views.modificar_producto,name='modificar_producto'),
    path('eliminar-producto/<id>',views.eliminar_producto,name='eliminar_producto'),
    path('registro', views.registro, name='registro'),
    path('api/', include(router.urls)),
]