from django.db import models
from entradas.models import Cliente
from entradas.models import Producto
# Create your models here.
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)  # Asegúrate de que exista un producto con ID=1
    cantidad = models.PositiveIntegerField(default=0)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    fecha_venta = models.DateField()

    class Meta:
        ordering = ('-fecha_venta',)

    def __str__(self):
        return f"{self.cliente} - {self.fecha_venta} - {self.producto} - {self.cantidad} - {self.precio_total}"
        
    def save(self, *args, **kwargs):
        # Calcular el precio total antes de guardar
        if self.producto and self.cantidad:
            self.precio_total = self.cantidad * self.producto.precio_venta
 # Asegúrate de que Producto tenga un campo 'precio'
        else:
            self.precio_total = 0  # Valor predeterminado si falta algún dato
        super().save(*args, **kwargs)
