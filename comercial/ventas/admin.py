from django.contrib import admin
from .models import Venta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_venta', 'producto', 'cantidad', 'precio_total')
    search_fields = ('cliente', 'fecha_venta', 'producto', 'cantidad', 'precio_total')
    list_filter = ('cliente', 'fecha_venta', 'producto', 'cantidad', 'precio_total')
    ordering = ('-fecha_venta',)

