from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from rest_framework import viewsets, permissions
from ..serializer import DespachoSerializer
from ..models import Despacho, Ruta, Vehiculo, Aeronave, Conductor, Piloto, Carga
from ..utils import requiere_token
from django.db.models import Q

# LISTADO
def lista_despacho(request):

    fecha = request.GET.get("fecha", "")
    estado = request.GET.get("estado", "")
    costo = request.GET.get("costo", "")
    tipo_transporte = request.GET.get("tipo_transporte", "")
    ruta = request.GET.get("ruta", "")
    operador = request.GET.get("operador", "")


    despachos = Despacho.objects.all().order_by("-fecha_despacho")

    # Filtros
    if fecha:
        despachos = despachos.filter(fecha_despacho=fecha)

    if estado:
        despachos = despachos.filter(estado=estado)

    if costo:
        despachos = despachos.filter(costo_envio__gte=costo)

    if tipo_transporte:
        despachos = despachos.filter(ruta_id__tipo_transporte=tipo_transporte)
        #  ↑ ESTA ES LA CORRECCIÓN IMPORTANTE
    if ruta:
        despachos = despachos.filter(
            Q(ruta_id__origen__icontains=ruta) | Q(ruta_id__destino__icontains=ruta)
        )
    if operador:
        despachos = despachos.filter(
            Q(conductor_id__nombre__icontains=operador) |
            Q(piloto_id__nombre__icontains=operador) 
        )
    # Paginación
    paginator = Paginator(despachos, 10)
    page = request.GET.get("page")
    despachos = paginator.get_page(page)

    context = {
        "despachos": despachos,
        "fecha": fecha,
        "estado": estado,
        "costo": costo,
        "tipo_transporte": tipo_transporte,
        "ruta": ruta, 
        "operador": operador,
    }

    return render(request, "transporte/Despacho/lista_despacho.html", context)

# CREAR
@requiere_token
def crear_despacho(request):

    ruta = Ruta.objects.all()
    vehiculos = Vehiculo.objects.all()
    aeronaves = Aeronave.objects.all()
    conductores = Conductor.objects.all()
    pilotos = Piloto.objects.all()
    cargas = Carga.objects.all()

    if request.method == "POST":
        try:
            fecha = request.POST.get("fecha_despacho")
            estado = request.POST.get("estado")
            costo = request.POST.get("costo_envio")
            ruta = request.POST.get("ruta_id")
            vehiculo = request.POST.get("vehiculo_id")
            aeronave = request.POST.get("aeronave_id")
            conductor = request.POST.get("conductor_id")
            piloto = request.POST.get("piloto_id")
            carga = request.POST.get("carga_id")

            Despacho.objects.create(
                fecha_despacho=fecha,
                estado=estado,
                costo_envio=costo,
                ruta_id_id=ruta,
                vehiculo_id_id=vehiculo,
                aeronave_id_id=aeronave if aeronave else None,
                conductor_id_id=conductor if conductor else None,
                piloto_id_id=piloto if piloto else None,
                carga_id_id=carga,
            )

            messages.success(request, "Despacho creado correctamente.")
            return redirect("lista_despacho")

        except Exception as e:
            messages.error(request, f"Error al crear el despacho: {e}")

    return render(request, "transporte/Despacho/crear_despacho.html", {
        "ruta": ruta,
        "vehiculos": vehiculos,
        "aeronaves": aeronaves,
        "conductores": conductores,
        "pilotos": pilotos,
        "cargas": cargas,
    })

# EDITAR
@requiere_token
def editar_despacho(request, id):
    despacho = Despacho.objects.get(id=id)

    ruta = Ruta.objects.all()
    vehiculos = Vehiculo.objects.all()
    aeronaves = Aeronave.objects.all()
    conductores = Conductor.objects.all()
    pilotos = Piloto.objects.all()
    cargas = Carga.objects.all()

    if request.method == "POST":
        try:
            fecha = request.POST.get("fecha_despacho")
            estado = request.POST.get("estado")
            costo = request.POST.get("costo_envio")
            ruta_id = request.POST.get("ruta_id")
            vehiculo_id = request.POST.get("vehiculo_id")
            aeronave_id = request.POST.get("aeronave_id")
            conductor_id = request.POST.get("conductor_id")
            piloto_id = request.POST.get("piloto_id")
            carga_id = request.POST.get("carga_id")
            tipo_transporte = request.POST.get("tipo_transporte")

            # Validar tipo de transporte
            if tipo_transporte == "terrestre":
                aeronave_id = None
                piloto_id = None
            elif tipo_transporte == "aereo":
                vehiculo_id = None
                conductor_id = None
            else:
                messages.error(request, "Debes seleccionar un tipo de transporte válido.")
                return redirect("editar_despacho", id=id)

            # Actualizar despacho
            despacho.fecha_despacho = fecha
            despacho.estado = estado
            despacho.costo_envio = costo
            despacho.ruta_id_id = ruta_id
            despacho.vehiculo_id_id = vehiculo_id
            despacho.aeronave_id_id = aeronave_id
            despacho.conductor_id_id = conductor_id
            despacho.piloto_id_id = piloto_id
            despacho.carga_id_id = carga_id

            despacho.save()

            messages.success(request, "Despacho actualizado correctamente.")
            return redirect("lista_despacho")

        except Exception as e:
            messages.error(request, f"Error al actualizar el despacho: {e}")

    contexto = {
        "despacho": despacho,
        "ruta": ruta,
        "vehiculos": vehiculos,
        "aeronaves": aeronaves,
        "conductores": conductores,
        "pilotos": pilotos,
        "cargas": cargas,
    }

    return render(request, "transporte/Despacho/editar_despacho.html", contexto)

# ELIMINAR
@requiere_token
def eliminar_despacho(request, id):
    despacho = get_object_or_404(Despacho, id=id)

    if request.method == 'POST':
        despacho.delete()
        return redirect('lista_despacho')

    return render(request, 'transporte/Despacho/eliminar_despacho.html', {
        'despacho': despacho
    })