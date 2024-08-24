from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        
        # # Campos escolhidos
        # fields = ['nome', 'cpf', 'telefone','habilitacao']

        # Todos os campos
        fields = '__all__'
