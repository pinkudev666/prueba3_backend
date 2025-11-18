from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions
from ..serializer import PilotoSerializer
from ..models import Piloto
from ..utils import requiere_token

# LISTADO
def lista_piloto(request):
    # --- 1. OBTENER FILTROS ---
    search = request.GET.get("search", "")             # búsqueda por nombre o rut
    estado = request.GET.get("estado", "")             # activo / inactivo

    # --- 2. QUERY BASE ---
    pilotos = Piloto.objects.all()

    # --- 3. FILTRO BÚSQUEDA ---
    if search:
        pilotos = pilotos.filter(
            nombre__icontains=search
        ) | pilotos.filter(rut__icontains=search)

    # --- 4. FILTRO ESTADO ---
    if estado == "activo":
        pilotos = pilotos.filter(activo=True)
    elif estado == "inactivo":
        pilotos = pilotos.filter(activo=False)

    # --- 5. PAGINACIÓN ---
    paginator = Paginator(pilotos, 5)  # 5 pilotos por página
    page = request.GET.get("page")
    pilotos_paginados = paginator.get_page(page)

    # --- 6. CONTEXTO ---
    context = {
        "pilotos": pilotos_paginados,
        "search": search,
        "estado": estado,
    }

    return render(request, "transporte/Piloto/lista_piloto.html", context)
# CREAR
@requiere_token
def crear_piloto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        rut = request.POST.get("rut")
        certificacion = request.POST.get("certificacion")
        activo = True if request.POST.get("activo") == "1" else False

        Piloto.objects.create(
            nombre=nombre,
            rut=rut,
            certificacion=certificacion,
            activo=activo
        )

        return redirect("lista_piloto")

    return render(request, "transporte/Piloto/crear_piloto.html")

# EDITAR
@requiere_token
def editar_piloto(request, id):
    piloto = get_object_or_404(Piloto, id=id)

    if request.method == "POST":
        piloto.nombre = request.POST.get("nombre")
        piloto.rut = request.POST.get("rut")
        piloto.certificacion = request.POST.get("certificacion")
        piloto.activo = True if request.POST.get("activo") == "1" else False
        piloto.save()

        return redirect("lista_piloto")

    context = {
        "piloto": piloto
    }
    return render(request, "transporte/Piloto/editar_piloto.html", context)
# ELIMINAR
@requiere_token
def eliminar_piloto(request, id):
    piloto = get_object_or_404(Piloto, id=id)

    if request.method == "POST":
        piloto.delete()
        return redirect("lista_piloto")

    context = {
        "piloto": piloto
    }
    return render(request, "transporte/Piloto/eliminar_piloto.html", context)