from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions
from ..serializer import ConductorSerializer
from ..models import Conductor
from ..utils import requiere_token

# LISTADO
def lista_conductor(request):

    # --- FILTROS ---
    search = request.GET.get("search", "")
    estado = request.GET.get("estado", "")

    conductores = Conductor.objects.all()

    # Filtro búsqueda
    if search:
        conductores = conductores.filter(
            nombre__icontains=search
        ) | conductores.filter(
            rut__icontains=search
        )

    # Filtro por estado
    if estado == "activo":
        conductores = conductores.filter(activo=True)
    elif estado == "inactivo":
        conductores = conductores.filter(activo=False)

    # --- PAGINACIÓN ---
    paginator = Paginator(conductores, 5)  # 5 registros por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "transporte/Conductor/lista_conductor.html", {
        "page_obj": page_obj,
        "search": search,
        "estado": estado,
    })
# CREAR
@requiere_token
def crear_conductor(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        rut = request.POST.get("rut")
        licencia = request.POST.get("licencia")
        activo = request.POST.get("activo") == "1"   # Convierte "1" en True, "0" en False

        Conductor.objects.create(
            nombre=nombre,
            rut=rut,
            licencia=licencia,
            activo=activo
        )

        return redirect("lista_conductor")  # Nombre de tu listado

    return render(request, "transporte/Conductor/crear_conductor.html")

# EDITAR
@requiere_token
def editar_conductor(request, id):
    conductor = get_object_or_404(Conductor, id=id)

    if request.method == "POST":
        conductor.nombre = request.POST.get("nombre")
        conductor.rut = request.POST.get("rut")
        conductor.licencia = request.POST.get("licencia")
        conductor.activo = request.POST.get("activo") == "1"
        conductor.save()

        return redirect("lista_conductor")

    return render(request, "transporte/Conductor/editar_conductor.html", {"conductor": conductor})
# ELIMINAR
@requiere_token
def eliminar_conductor(request, id):
    conductor = get_object_or_404(Conductor, id=id)

    if request.method == "POST":
        conductor.delete()
        return redirect("lista_conductor")

    return render(request, "transporte/Conductor/eliminar_conductor.html", {"conductor": conductor})