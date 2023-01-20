from rest_framework import viewsets, filters
from prova.serializers import ClienteSerializer
from .models import Cliente
from .serializers import ClienteSerializer
import pandas as pd
import io
import datetime
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.filter(sexo='F',cidade='Meeren')
    def create(self, request):
        response=''
        print("inserindo")
        arquivo=request.FILES.get('nome_arquivo')
        scores = pd.read_excel(arquivo,engine="openpyxl")
        response='Carregado'
        
        for i in range (len(scores)):
            d=datetime.datetime.fromtimestamp(scores['nascimento'][i]/1e3)
            c=Cliente(nome=scores['nome'][i],sobrenome=scores['sobrenome'][i],sexo=scores['sexo'][i],altura=scores['altura'][i],peso=scores['peso'][i],nascimento=d,bairro=scores['bairro'][i],cidade=scores['cidade'][i],estado=scores['estado'][i],numero=scores['numero'][i],codigo=scores['id'][i],nome_arquivo=arquivo)
            c.save()
            
        return Response(response)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter] #novo
    ordering_fields = ['nascimento',] #ordenar por idade
    filterset_fields = ['sexo']
class FiltrarViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    def create(self, request):
        response=''
        arquivo=request.FILES.get('nome_arquivo')
        scores = pd.read_excel(arquivo,engine="openpyxl")
        response='Carregado'
        for i in range (len(scores)):
            d=datetime.datetime.fromtimestamp(scores['nascimento'][i]/1e3)
            c=Cliente(nome=scores['nome'][i],sobrenome=scores['sobrenome'][i],sexo=scores['sexo'][i],altura=scores['altura'][i],peso=scores['peso'][i],nascimento=d,bairro=scores['bairro'][i],cidade=scores['cidade'][i],estado=scores['estado'][i],numero=scores['numero'][i],codigo=scores['id'][i],nome_arquivo=arquivo)
            c.save()
        return Response(response)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter] #novo
    ordering_fields = ['nascimento',] #ordenar por idade
    filterset_fields = ['sexo']
    
'''class FiltrarViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class UploadViewSet(viewsets.ModelViewSet):
    
    def create(self, request):
        arquivo=request.FILES.get('nome_arquivo')
        scores = pd.read_excel(arquivo,engine="openpyxl")
        response='Carregado'
        print('create')
        for i in range (len(scores)):
            d=datetime.datetime.fromtimestamp(scores['nascimento'][i]/1e3)
            c=Cliente(nome=scores['nome'][i],sobrenome=scores['sobrenome'][i],sexo=scores['sexo'][i],altura=scores['altura'][i],peso=scores['peso'][i],nascimento=d,bairro=scores['bairro'][i],cidade=scores['cidade'][i],estado=scores['estado'][i],numero=scores['numero'][i],codigo=scores['id'][i],nome_arquivo=arquivo)
            c.save()
        return Response(response)'''