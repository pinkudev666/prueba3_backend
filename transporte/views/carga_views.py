from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions
from ..serializer import CargaSerializer
from ..models import Carga,Cliente
from ..utils import requiere_token

# LISTADO
@requiere_token
def lista_carga(request):
    cargas = Carga.objects.select_related("cliente_id").all()

    # 🔎 FILTROS
    cliente = request.GET.get("cliente")
    tipo = request.GET.get("tipo")
    peso_valor = request.GET.get("peso_valor")

    if cliente:
        cargas = cargas.filter(cliente_id__nombre__icontains=cliente)

    if tipo:
        cargas = cargas.filter(tipo__icontains=tipo)

    if peso_valor:
        cargas = cargas.filter(peso__icontains=peso_valor) | cargas.filter(valor__icontains=peso_valor)

    # 📄 PAGINACIÓN
    paginator = Paginator(cargas, 10)  # 10 resultados por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "cliente": cliente or "",
        "tipo": tipo or "",
        "peso_valor": peso_valor or "",
    }

    return render(request, "transporte/Carga/lista_carga.html", context)
# CREAR
def crear_carga(request):
    clientes = Cliente.objects.all()

    if request.method == "POST":
        cliente_id = request.POST.get("cliente_id")
        peso = request.POST.get("peso")
        tipo = request.POST.get("tipo")
        valor = request.POST.get("valor")

        Carga.objects.create(
            cliente_id_id=cliente_id,
            peso=peso,
            tipo=tipo,
            valor=valor
        )

        return redirect("lista_carga")

    return render(request, "transporte/Carga/crear_carga.html", {"clientes": clientes})

# EDITAR
def editar_carga(request, id):
    carga = get_object_or_404(Carga, id=id)
    clientes = Cliente.objects.all()

    if request.method == "POST":
        carga.cliente_id_id = request.POST.get("cliente_id")
        carga.peso = request.POST.get("peso")
        carga.tipo = request.POST.get("tipo")
        carga.valor = request.POST.get("valor")
        carga.save()

        return redirect("lista_carga")

    return render(request, "transporte/Carga/editar_carga.html", {
        "carga": carga,
        "clientes": clientes
    })
# ELIMINAR
def eliminar_carga(request, id):
    carga = get_object_or_404(Carga, id=id)

    if request.method == "POST":
        carga.delete()
        return redirect("lista_carga")

    return render(request, "transporte/Carga/eliminar_carga.html", {"carga": carga})