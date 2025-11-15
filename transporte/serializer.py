from rest_framework import serializers
from .models import *

class RutaSerializer(serializers.ModelSerializer):
    despacho = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Ruta
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    despacho = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Vehiculo
        fields = '__all__'

class AeronaveSerializer(serializers.ModelSerializer):
    despacho = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Aeronave
        fields = '__all__'

class ConductorSerializer(serializers.ModelSerializer):
    despacho = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Conductor
        fields = '__all__'

class PilotoSerializer(serializers.ModelSerializer):
    despacho = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Piloto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    carga = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = '__all__'

class CargaSerializer(serializers.ModelSerializer):
    despacho = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    cliente = ClienteSerializer(read_only=True)
    class Meta:
        model = Carga
        fields = '__all__'

class DespachoSerializer(serializers.ModelSerializer):
    ruta = RutaSerializer(read_only=True)
    vehiculo = VehiculoSerializer(read_only=True)
    aeronave = AeronaveSerializer(read_only=True)
    conductor = ConductorSerializer(read_only=True)
    piloto = PilotoSerializer(read_only=True)
    carga = CargaSerializer(read_only=True)
    class Meta:
        model = Despacho
        fields = '__all__'

