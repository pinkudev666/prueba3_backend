from django.urls import path, include
from rest_framework import routers
from transporte import views

router = routers.DefaultRouter() 
router.register(r'rutas', views.RutaViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'aeronaves', views.AeronaveViewSet)
router.register(r'conductores', views.ConductorViewSet)
router.register(r'pilotos', views.PilotoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'cargas', views.CargaViewSet)
router.register(r'despachos', views.DespachoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]