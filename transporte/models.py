from django.db import models

# Create your models here.
class Ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    tipo_transporte = models.CharField(max_length=100)
    distancia_km = models.IntegerField()

class Vehiculo(models.Model):
    patente = models.CharField(max_length=100)
    tipo_vehiculo = models.CharField(max_length=100)
    capacidad_kg = models.IntegerField()
    activo = models.BooleanField(default=True)

class Aeronave(models.Model):
    matricula = models.CharField(max_length=100)
    tipo_aeronave = models.CharField(max_length=100)
    capacidad_kg = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    licencia = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    certificacion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

class Despacho(models.Model):
    ESTADOS:{
        (),
        (),
    }
    fecha_despacho = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    costo_envio = models.IntegerField()
    ruta_id = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name="despacho")
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name="despacho")
    aeronave_id = models.ForeignKey(Aeronave, on_delete=models.CASCADE, related_name="despacho")
    conductor_id = models.ForeignKey(Conductor, on_delete=models.CASCADE, related_name="despacho")
    piloto_id = models.ForeignKey(Piloto, on_delete=models.CASCADE, related_name="despacho")
