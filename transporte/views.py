from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import *
from .models import *

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    permission_classes = [permissions.IsAuthenticated] 

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class AeronaveViewSet(viewsets.ModelViewSet):
    queryset = Aeronave.objects.all()
    serializer_class = AeronaveSerializer

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
    permission_classes = [permissions.IsAuthenticated] 

class PilotoViewSet(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    permission_classes = [permissions.IsAuthenticated] 

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CargaViewSet(viewsets.ModelViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    permission_classes = [permissions.IsAuthenticated] 

class DespachoViewSet(viewsets.ModelViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer

def inicio(request):
    return render(request, "transporte/inicio.html")

def servicios(request):
    return render(request, "transporte/servicios.html")

def nosotros(request):
    return render(request, "transporte/nosotros.html")

def inicio_sesion(request):
    return render(request, "transporte/inicio_sesion.html")

def documentacion(request):
    return render(request, "transporte/documentacion.html")
#------------------------------------------------------------------------------------

def lista_ruta(request):
    rutas = Ruta.objects.all()
    return render(request, 'transporte/Ruta/lista_ruta.html', {'rutas': rutas})

#------------------------------------------------------------------------------------
# LISTADO
def lista_aeronave(request):
    return render(request, 'transporte/Aeronave/lista_aeronave.html')
# CREAR
def crear_aeronave(request):
    return render(request, 'transporte/Aeronave/crear_aeronave.html')

# EDITAR
def editar_aeronave(request, id):
    return render(request, 'transporte/Aeronave/editar_aeronave.html', {"id": id})
# ELIMINAR
def eliminar_aeronave(request, id):
    return render(request, 'transporte/Aeronave/eliminar_aeronave.html', {"id": id})

#------------------------------------------------------------------------------------
# LISTADO
def lista_vehiculo(request):
    return render(request, 'transporte/Vehiculo/lista_vehiculo.html')
# CREAR
def crear_vehiculo(request):
    return render(request, 'transporte/Vehiculo/crear_vehiculo.html')

# EDITAR
def editar_vehiculo(request, id):
    return render(request, 'transporte/Vehiculo/editar_vehiculo.html', {"id": id})
# ELIMINAR
def eliminar_vehiculo(request, id):
    return render(request, 'transporte/Vehiculo/eliminar_vehiculo.html', {"id": id})
#------------------------------------------------------------------------------------
# LISTADO
def lista_conductor(request):
    return render(request, 'transporte/Conductor/lista_conductor.html')
# CREAR
def crear_conductor(request):
    return render(request, 'transporte/Conductor/crear_conductor.html')

# EDITAR
def editar_conductor(request, id):
    return render(request, 'transporte/Conductor/editar_conductor.html', {"id": id})
# ELIMINAR
def eliminar_conductor(request, id):
    return render(request, 'transporte/Conductor/eliminar_conductor.html', {"id": id})
#------------------------------------------------------------------------------------
# LISTADO
def lista_piloto(request):
    return render(request, 'transporte/Piloto/lista_piloto.html')
# CREAR
def crear_piloto(request):
    return render(request, 'transporte/Piloto/crear_piloto.html')

# EDITAR
def editar_piloto(request, id):
    return render(request, 'transporte/Piloto/editar_piloto.html', {"id": id})
# ELIMINAR
def eliminar_piloto(request, id):
    return render(request, 'transporte/Piloto/eliminar_piloto.html', {"id": id})
#------------------------------------------------------------------------------------
# LISTADO
def lista_ruta(request):
    return render(request, 'transporte/Ruta/lista_ruta.html')
# CREAR
def crear_ruta(request):
    return render(request, 'transporte/Ruta/crear_ruta.html')

# EDITAR
def editar_ruta(request, id):
    return render(request, 'transporte/Ruta/editar_ruta.html', {"id": id})
# ELIMINAR
def eliminar_ruta(request, id):
    return render(request, 'transporte/Ruta/eliminar_ruta.html', {"id": id})
#------------------------------------------------------------------------------------
# LISTADO
def lista_despacho(request):
    return render(request, 'transporte/Despacho/lista_despacho.html')
# CREAR
def crear_despacho(request):
    return render(request, 'transporte/Despacho/crear_despacho.html')

# EDITAR
def editar_despacho(request, id):
    return render(request, 'transporte/Despacho/editar_despacho.html', {"id": id})
# ELIMINAR
def eliminar_despacho(request, id):
    return render(request, 'transporte/Despacho/eliminar_despacho.html', {"id": id})
#------------------------------------------------------------------------------------
# LISTADO
def lista_cliente(request):
    return render(request, 'transporte/Cliente/lista_cliente.html')
# CREAR
def crear_cliente(request):
    return render(request, 'transporte/Cliente/crear_cliente.html')

# EDITAR
def editar_cliente(request, id):
    return render(request, 'transporte/Cliente/editar_cliente.html', {"id": id})
# ELIMINAR
def eliminar_cliente(request, id):
    return render(request, 'transporte/Cliente/eliminar_cliente.html', {"id": id})
#------------------------------------------------------------------------------------
# LISTADO
def lista_carga(request):
    return render(request, 'transporte/Carga/lista_carga.html')
# CREAR
def crear_carga(request):
    return render(request, 'transporte/Carga/crear_carga.html')

# EDITAR
def editar_carga(request, id):
    return render(request, 'transporte/Carga/editar_carga.html', {"id": id})
# ELIMINAR
def eliminar_carga(request, id):
    return render(request, 'transporte/Carga/eliminar_carga.html', {"id": id})
#------------------------------------------------------------------------------------