from django.contrib import admin
from .models import Contacto, Marca, Producto
from .forms import ProductoForm

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre","precio","nuevo","marca"]
    list_editable=["precio"]
    search_fields=["nombre"]
    list_filter=["marca","nuevo"]

    form = ProductoForm
    #list_per_page=1
admin.site.register(Marca)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Contacto)