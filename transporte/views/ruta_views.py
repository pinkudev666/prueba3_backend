from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions
from ..serializer import rutaerializer
from ..models import Ruta
from ..utils import requiere_token

# LISTADO
@requiere_token
def lista_ruta(request):
    # Obtener todos los registros
    ruta = Ruta.objects.all()

    # Filtros
    q = request.GET.get('q', '')  # búsqueda por origen o destino
    tipo = request.GET.get('tipo', '')  # tipo de transporte
    distancia = request.GET.get('distancia', '')  # distancia mínima

    if q:
        ruta = ruta.filter(origen__icontains=q) | ruta.filter(destino__icontains=q)
    if tipo:
        ruta = ruta.filter(tipo_transporte=tipo)
    if distancia:
        try:
            ruta = ruta.filter(distancia_km__gte=int(distancia))
        except ValueError:
            pass  # ignorar si no es un número válido

    # Paginación
    paginator = Paginator(ruta, 5)  # 5 ruta por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'transporte/Ruta/lista_ruta.html', {
        'page_obj': page_obj,
        'q': q,
        'tipo': tipo,
        'distancia': distancia,
    })
# CREAR
def crear_ruta(request):
    if request.method == 'POST':
        origen = request.POST.get('origen')
        destino = request.POST.get('destino')
        tipo_transporte = request.POST.get('tipo_transporte')
        distancia = request.POST.get('distancia')

        # Validar que todos los campos tengan datos
        if origen and destino and tipo_transporte and distancia:
            try:
                distancia = int(distancia)
                Ruta.objects.create(
                    origen=origen,
                    destino=destino,
                    tipo_transporte=tipo_transporte,
                    distancia_km=distancia
                )
                return redirect('lista_ruta')  # redirigir al listado
            except ValueError:
                error = "La distancia debe ser un número."
        else:
            error = "Todos los campos son obligatorios."
    else:
        error = None

    return render(request, 'transporte/Ruta/crear_ruta.html', {'error': error})

# EDITAR
def editar_ruta(request, id):
    ruta = get_object_or_404(Ruta, id=id)
    error = None

    if request.method == 'POST':
        origen = request.POST.get('origen')
        destino = request.POST.get('destino')
        tipo_transporte = request.POST.get('tipo_transporte')
        distancia = request.POST.get('distancia')

        if origen and destino and tipo_transporte and distancia:
            try:
                distancia = int(distancia)
                ruta.origen = origen
                ruta.destino = destino
                ruta.tipo_transporte = tipo_transporte
                ruta.distancia_km = distancia
                ruta.save()
                return redirect('lista_ruta')
            except ValueError:
                error = "La distancia debe ser un número."
        else:
            error = "Todos los campos son obligatorios."

    return render(request, 'transporte/Ruta/editar_ruta.html', {
        'ruta': ruta,
        'error': error
    })
# ELIMINAR
def eliminar_ruta(request, id):
    ruta = get_object_or_404(Ruta, id=id)
    
    if request.method == 'POST':
        ruta.delete()
        return redirect('lista_ruta')  # Redirige al listado después de eliminar

    return render(request, 'transporte/Ruta/eliminar_ruta.html', {'ruta': ruta})