from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Ruta(models.Model):
    TIPO_TRANSPORTE = [
        ('T','TERRESTRE'),
        ('A','AEREO'),
    ]
    origen = models.CharField(max_length=500)
    destino = models.CharField(max_length=500)
    tipo_transporte = models.CharField(max_length=100, choices= TIPO_TRANSPORTE)
    distancia_km = models.IntegerField()
    def __str__(self):
        return f"{self.origen} {self.destino}"

class Vehiculo(models.Model):
    patente = models.CharField(max_length=100)
    tipo_vehiculo = models.CharField(max_length=100)
    capacidad_kg = models.IntegerField()
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.patente

class Aeronave(models.Model):
    matricula = models.CharField(max_length=100)
    tipo_aeronave = models.CharField(max_length=100)
    capacidad_kg = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.matricula

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    licencia = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    certificacion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):   
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Carga(models.Model):       
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="carga")
    peso = models.IntegerField()
    tipo = models.CharField(max_length=100)
    valor = models.IntegerField()
    def __str__(self):
        return f"{self.tipo} {self.valor}"

class Despacho(models.Model):
    ESTADOS = [
        ('ER','EN RUTA'),
        ('E', 'ENTREGADO'),
        ('P', 'PENDIENTE')
    ]
    fecha_despacho = models.DateField()
    estado = models.CharField(max_length=50, choices=ESTADOS)
    costo_envio = models.IntegerField()
    ruta_id = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name="despacho")
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True, blank=True, related_name="despacho")
    aeronave_id = models.ForeignKey(Aeronave, on_delete=models.CASCADE, null=True, blank=True, related_name="despacho")
    conductor_id = models.ForeignKey(Conductor, on_delete=models.CASCADE, null=True, blank=True, related_name="despacho")
    piloto_id = models.ForeignKey(Piloto, on_delete=models.CASCADE, null=True, blank=True, related_name="despacho")    
    carga_id = models.ForeignKey(Carga, on_delete=models.CASCADE, related_name="despacho")

    def __str__(self):
        return f"{self.carga_id.tipo} {self.fecha_despacho} {self.estado}"