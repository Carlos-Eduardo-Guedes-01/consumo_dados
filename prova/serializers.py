from rest_framework import serializers
from prova.models import Cliente,Cliente2

class ClienteSerializer(serializers.ModelSerializer):
    arquivo=[]
    class Meta:
        model = Cliente
        arquivo=fields = ['nome_arquivo','codigo','nome','sobrenome','sexo','altura','peso','nascimento','estado','cidade','bairro','numero']
class Cliente2Serializer(serializers.ModelSerializer):
    arquivo=[]
    class Meta:
        model = Cliente2
        arquivo=fields = ['nome_arquivo','codigo','nome','sobrenome','sexo','altura','peso','nascimento','estado','cidade','bairro','numero']
