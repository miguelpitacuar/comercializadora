from rest_framework import viewsets
from ventas.models import Venta
from ventas.serealizers import VentaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


