from django.urls import path, include
from rest_framework import routers
from transporte import views   # <--- ESTA ES LA IMPORTACIÓN CORRECTA

router = routers.DefaultRouter() 
router.register(r'ruta', views.RutaViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'aeronaves', views.AeronaveViewSet)
router.register(r'conductores', views.ConductorViewSet)
router.register(r'pilotos', views.PilotoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'cargas', views.CargaViewSet)
router.register(r'despachos', views.DespachoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # ------------------ RUTA ------------------
    path('ruta/', views.lista_ruta, name='lista_ruta'),
    path('ruta/crear/', views.crear_ruta, name='crear_ruta'),
    path('ruta/editar/<int:id>/', views.editar_ruta, name='editar_ruta'),
    path('ruta/eliminar/<int:id>/', views.eliminar_ruta, name='eliminar_ruta'),

    # ---------------- AERONAVE ----------------
    path('aeronave/', views.lista_aeronave, name='lista_aeronave'),
    path('aeronave/crear/', views.crear_aeronave, name='crear_aeronave'),
    path('aeronave/editar/<int:id>/', views.editar_aeronave, name='editar_aeronave'),
    path('aeronave/eliminar/<int:id>/', views.eliminar_aeronave, name='eliminar_aeronave'),

    # ---------------- VEHICULO ----------------
    path('vehiculo/', views.lista_vehiculo, name='lista_vehiculo'),
    path('vehiculo/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculo/editar/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculo/eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),

    # ---------------- CONDUCTOR ----------------
    path('conductor/', views.lista_conductor, name='lista_conductor'),
    path('conductor/crear/', views.crear_conductor, name='crear_conductor'),
    path('conductor/editar/<int:id>/', views.editar_conductor, name='editar_conductor'),
    path('conductor/eliminar/<int:id>/', views.eliminar_conductor, name='eliminar_conductor'),

    # ---------------- PILOTO ----------------
    path('piloto/', views.lista_piloto, name='lista_piloto'),
    path('piloto/crear/', views.crear_piloto, name='crear_piloto'),
    path('piloto/editar/<int:id>/', views.editar_piloto, name='editar_piloto'),
    path('piloto/eliminar/<int:id>/', views.eliminar_piloto, name='eliminar_piloto'),

    # ---------------- DESPACHO ----------------
    path('despacho/', views.lista_despacho, name='lista_despacho'),
    path('despacho/crear/', views.crear_despacho, name='crear_despacho'),
    path('despacho/editar/<int:id>/', views.editar_despacho, name='editar_despacho'),
    path('despacho/eliminar/<int:id>/', views.eliminar_despacho, name='eliminar_despacho'),

    # ---------------- CLIENTE ----------------
    path('cliente/', views.lista_cliente, name='lista_cliente'),
    path('cliente/crear/', views.crear_cliente, name='crear_cliente'),
    path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('cliente/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),

    # ---------------- CARGA ----------------
    path('carga/', views.lista_carga, name='lista_carga'),
    path('carga/crear/', views.crear_carga, name='crear_carga'),
    path('carga/editar/<int:id>/', views.editar_carga, name='editar_carga'),
    path('carga/eliminar/<int:id>/', views.eliminar_carga, name='eliminar_carga'),
]
