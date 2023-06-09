from django.contrib import admin
from .models import ProductosModel

# Register your models here.

class ProductosModelAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'descripcion', 'precio', 'imagen_url', 'estado')

admin.site.register(ProductosModel, ProductosModelAdmin)