from django.db import models
from entradas.models import Cliente
# Create your models here.
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateField()

    class Meta:
        ordering = ('-fecha_venta',)

    def __str__(self):
        return f"{self.cliente} - {self.fecha_venta}"
        
