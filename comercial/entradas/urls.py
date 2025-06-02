from rest_framework import routers
from .api import ProductoViewSet   
from .api import BodegaViewSet
from .api import TipoProductoViewSet
from .api import UnidadMedidaViewSet
from .api import ProveedorViewSet
from .api import ClienteViewSet
from .api import EstadoFacturaViewSet
from .api import TipoFacturaViewSet
from .api import EntradaViewSet
from .api import FacturaEntradaViewSet
from .api import SalidaViewSet
from .api import FacturaSalidaViewSet
from .api import ReportePerdidaViewSet

router=  routers.DefaultRouter()

router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/bodegas', BodegaViewSet, 'bodegas')
router.register('api/tipoProducto', TipoProductoViewSet, 'tipoProducto')
router.register('api/unidadMedida', UnidadMedidaViewSet, 'unidadMedida')
router.register('api/proveedores', ProveedorViewSet, 'proveedores')
router.register('api/clientes', ClienteViewSet, 'clientes')
router.register('api/estadoFactura', EstadoFacturaViewSet, 'estadoFactura')
router.register('api/tipoFactura', TipoFacturaViewSet, 'tipoFactura')
router.register('api/entradas', EntradaViewSet, 'entradas')
router.register('api/facturaEntrada', FacturaEntradaViewSet, 'facturaEntrada')
router.register('api/salidas', SalidaViewSet, 'salidas')
router.register('api/facturaSalida', FacturaSalidaViewSet, 'facturaSalida')
router.register('api/reportePerdida', ReportePerdidaViewSet, 'reportePerdida')

urlpatterns = router.urls
