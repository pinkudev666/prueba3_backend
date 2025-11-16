from django.contrib import admin
from django.urls import path, include, re_path
from transporte.views import inicio,servicios, nosotros, inicio_sesion, documentacion
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentación de mi API",
        default_version='v1',
        description="Descripción de la API generada automáticamente",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@miapi.local"),
        license=openapi.License(name="Licencia MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),
    # Página de inicio
    path('', inicio, name='inicio'),
    path('servicios/', servicios, name='servicios'),
    path('nosotros/', nosotros, name='nosotros'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),    
    path('documentacion/', documentacion, name='documentacion'),
    # Rutas de la API REST
    path('transporte/', include('transporte.urls')),

    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Redoc UI (alternativa más minimalista)
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Configuración para servir archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "static")

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)