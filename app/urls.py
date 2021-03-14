from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/',views.contacto,name='contacto'),
    path('galeria/',views.galeria,name='galeria'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('productos/',views.listar_productos,name='listar_productos'),
    path('modificar-producto/<id>',views.modificar_producto,name='modificar_producto'),
    path('eliminar-producto/<id>',views.eliminar_producto,name='eliminar_producto')
]