from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions
from ..serializer import VehiculoSerializer
from ..models import Vehiculo
# LISTADO
def lista_vehiculo(request):
    # Obtener parámetros de búsqueda y filtro
    busqueda = request.GET.get('busqueda', '')
    tipo = request.GET.get('tipo', '')
    estado = request.GET.get('estado', '')

    vehiculos = Vehiculo.objects.all()

    # Aplicar filtros
    if busqueda:
        vehiculos = vehiculos.filter(patente__icontains=busqueda)
    if tipo:
        vehiculos = vehiculos.filter(tipo_vehiculo__icontains=tipo)
    if estado:
        if estado.lower() == 'activo':
            vehiculos = vehiculos.filter(activo=True)
        elif estado.lower() == 'inactivo':
            vehiculos = vehiculos.filter(activo=False)

    # Paginación (5 elementos por página)
    paginator = Paginator(vehiculos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'vehiculos': page_obj,
        'busqueda': busqueda,
        'tipo': tipo,
        'estado': estado,
    }
    return render(request, 'transporte/Vehiculo/lista_vehiculo.html', context)
# CREAR
def crear_vehiculo(request):
    if request.method == "POST":
        patente = request.POST.get('patente')
        tipo_vehiculo = request.POST.get('tipo_vehiculo')
        capacidad_kg = request.POST.get('capacidad_kg')
        activo = request.POST.get('activo') == "1"  # checkbox o select

        # Crear el vehículo en la base de datos
        Vehiculo.objects.create(
            patente=patente,
            tipo_vehiculo=tipo_vehiculo,
            capacidad_kg=capacidad_kg,
            activo=activo
        )
        return redirect('lista_vehiculo')  # Redirige al listado después de guardar

    return render(request, 'transporte/Vehiculo/crear_vehiculo.html')

# EDITAR
def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)

    if request.method == "POST":
        # Actualizar datos desde el formulario
        vehiculo.patente = request.POST.get('patente')
        vehiculo.tipo_vehiculo = request.POST.get('tipo_vehiculo')
        vehiculo.capacidad_kg = request.POST.get('capacidad_kg')
        vehiculo.activo = request.POST.get('activo') == "1"  # Convertir a booleano

        vehiculo.save()
        return redirect('lista_vehiculo')  # Redirige al listado después de guardar

    context = {
        'vehiculo': vehiculo
    }
    return render(request, 'transporte/Vehiculo/editar_vehiculo.html', context)
# ELIMINAR
def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)

    if request.method == "POST":
        vehiculo.delete()
        return redirect('lista_vehiculo')  # Redirige al listado después de eliminar

    context = {
        'vehiculo': vehiculo
    }
    return render(request, 'transporte/Vehiculo/eliminar_vehiculo.html', context)