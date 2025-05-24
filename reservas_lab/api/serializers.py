from rest_framework import serializers
from .models import User, Professor, Laboratorio, Reserva

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        