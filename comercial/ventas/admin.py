from django.contrib import admin
from .models import Venta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_venta')
    search_fields = ('cliente', 'fecha_venta')
    list_filter = ('cliente', 'fecha_venta')
    ordering = ('-fecha_venta',)

