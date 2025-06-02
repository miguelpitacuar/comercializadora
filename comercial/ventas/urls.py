from rest_framework import routers
from .api import VentaViewSet

router = routers.DefaultRouter()
router.register('ventas', VentaViewSet, 'ventas')

urlpatterns = router.urls