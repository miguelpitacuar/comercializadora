from entradas.models import Producto
from entradas.models import Bodega
from entradas.models import TipoProducto
from entradas.models import UnidadMedida
from entradas.models import Proveedor
from entradas.models import Cliente
from entradas.models import EstadoFactura
from entradas.models import TipoFactura
from entradas.models import Entrada
from entradas.models import FacturaEntrada
from entradas.models import Salida
from entradas.models import FacturaSalida
from entradas.models import ReportePerdida



from rest_framework import viewsets, permissions

from .serealizers import ProductoSerializer
from .serealizers import BodegaSerializer
from .serealizers import TipoProductoSerializer
from .serealizers import UnidadMedidaSerializer
from .serealizers import ProveedorSerializer
from .serealizers import ClienteSerializer
from .serealizers import EstadoFacturaSerializer
from .serealizers import TipoFacturaSerializer
from .serealizers import EntradaSerializer
from .serealizers import FacturaEntradaSerializer
from .serealizers import SalidaSerializer
from .serealizers import FacturaSalidaSerializer
from .serealizers import ReportePerdidaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BodegaSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoProductoSerializer

class UnidadMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadMedida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UnidadMedidaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

class EstadoFacturaViewSet(viewsets.ModelViewSet):
    queryset = EstadoFactura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstadoFacturaSerializer

class TipoFacturaViewSet(viewsets.ModelViewSet):
    queryset = TipoFactura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoFacturaSerializer

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EntradaSerializer

class FacturaEntradaViewSet(viewsets.ModelViewSet):
    queryset = FacturaEntrada.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacturaEntradaSerializer

class SalidaViewSet(viewsets.ModelViewSet):
    queryset = Salida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SalidaSerializer

class FacturaSalidaViewSet(viewsets.ModelViewSet):
    queryset = FacturaSalida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacturaSalidaSerializer

class ReportePerdidaViewSet(viewsets.ModelViewSet):
    queryset = ReportePerdida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReportePerdidaSerializer


    