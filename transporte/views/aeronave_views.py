from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions
from ..serializer import AeronaveSerializer
from ..models import Aeronave
# LISTADO
def lista_aeronave(request):
    # ----- FILTROS -----
    buscar = request.GET.get("buscar", "")
    tipo = request.GET.get("tipo", "")
    estado = request.GET.get("estado", "")
    aeronaves = Aeronave.objects.all()

    if buscar:
        aeronaves = aeronaves.filter(matricula__icontains=buscar)
    if tipo:
        aeronaves = aeronaves.filter(tipo_aeronave__icontains=tipo)
    if estado:
        if estado == "Activo":
            aeronaves = aeronaves.filter(activo=True)
        elif estado == "Inactivo":
            aeronaves = aeronaves.filter(activo=False)

    # ----- PAGINACIÓN -----
    paginator = Paginator(aeronaves, 5)  # 5 por página
    page = request.GET.get("page")
    aeronaves = paginator.get_page(page)

    return render(request, "transporte/Aeronave/lista_aeronave.html", {
        "aeronaves": aeronaves,
        "buscar": buscar,
        "tipo": tipo,
        "estado": estado
    })
# CREAR
def crear_aeronave(request):

    if request.method == "POST":
        matricula = request.POST.get("matricula")
        tipo = request.POST.get("tipo_aeronave")
        capacidad = request.POST.get("capacidad_kg")
        estado = request.POST.get("activo")

        Aeronave.objects.create(
            matricula=matricula,
            tipo_aeronave=tipo,
            capacidad_kg=capacidad,
            activo=True if estado == "1" else False
        )

        return redirect("lista_aeronave")

    return render(request, "transporte/Aeronave/crear_aeronave.html")

# EDITAR
def editar_aeronave(request, id):
    aeronave = get_object_or_404(Aeronave, id=id)

    if request.method == "POST":
        aeronave.matricula = request.POST.get("matricula")
        aeronave.tipo_aeronave = request.POST.get("tipo_aeronave")
        aeronave.capacidad_kg = request.POST.get("capacidad_kg")
        estado = request.POST.get("activo")
        aeronave.activo = True if estado == "1" else False

        aeronave.save()
        return redirect("lista_aeronave")

    return render(request, "transporte/Aeronave/editar_aeronave.html", {
        "aeronave": aeronave
    })

# ELIMINAR
def eliminar_aeronave(request, id):
    aeronave = get_object_or_404(Aeronave, id=id)

    if request.method == "POST":
        aeronave.delete()
        return redirect("lista_aeronave")

    return render(request, "transporte/Aeronave/eliminar_aeronave.html", {
        "aeronave": aeronave
    })