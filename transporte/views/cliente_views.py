from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions
from ..serializer import ClienteSerializer
from ..models import Cliente

# LISTADO
def lista_cliente(request):
    # Obtener parámetros del buscador
    q1 = request.GET.get('q1', '')  # nombre, apellido, RUT
    q2 = request.GET.get('q2', '')  # email, teléfono

    # Filtrar
    clientes = Cliente.objects.all()

    if q1:
        clientes = clientes.filter(
            rut__icontains=q1
        ) | clientes.filter(
            nombre__icontains=q1
        ) | clientes.filter(
            apellido__icontains=q1
        )

    if q2:
        clientes = clientes.filter(
            email__icontains=q2
        ) | clientes.filter(
            telefono__icontains=q2
        )

    # Paginación
    paginator = Paginator(clientes.order_by('id'), 10)  # 10 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'transporte/Cliente/lista_cliente.html', {
        'page_obj': page_obj,
        'q1': q1,
        'q2': q2,
    })
# CREAR
def crear_cliente(request):

    if request.method == "POST":
        rut = request.POST.get("rut")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        telefono = request.POST.get("telefono")
        email = request.POST.get("email")

        Cliente.objects.create(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email
        )

        return redirect('lista_cliente')

    return render(request, 'transporte/Cliente/crear_cliente.html')

# EDITAR
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.rut = request.POST.get("rut")
        cliente.nombre = request.POST.get("nombre")
        cliente.apellido = request.POST.get("apellido")
        cliente.telefono = request.POST.get("telefono")
        cliente.email = request.POST.get("email")

        cliente.save()
        return redirect('lista_cliente')

    return render(request, 'transporte/Cliente/editar_cliente.html', {
        'cliente': cliente
    })
# ELIMINAR
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.delete()
        return redirect('lista_cliente')

    return render(request, 'transporte/Cliente/eliminar_cliente.html', {
        'cliente': cliente
    })