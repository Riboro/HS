from rest_framework import serializers
from registro.models import Registro

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['nome', 'numero']


class ListarIdentificadorRegistroSerializer(serializers.ModelSerializer):
    #registro = serializers.ReadOnlyField(source='Registro.id')
    class Meta:
        model = Registro
        fields = ['nome']
