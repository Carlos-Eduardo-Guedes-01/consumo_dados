from django.db import models
class Cliente(models.Model):
    nome=models.CharField(max_length=200, null=True)
    sobrenome=models.CharField(max_length=200, null=True)
    sexo=models.CharField(max_length=3, null=True)
    altura=models.IntegerField(null=True)
    peso=models.FloatField(null=True)
    nascimento=models.DateField(null=True)
    bairro=models.CharField(max_length=200, null=True)
    cidade=models.CharField(max_length=200, null=True)
    estado=models.CharField(max_length=200, null=True)
    numero=models.IntegerField(null=True)
    nome_arquivo=models.FileField(null=True)
    codigo=models.IntegerField(null=True)
    def __str__(self):
        return self.nome
class Cliente2(models.Model):
    nome=models.CharField(max_length=200, null=True)
    sobrenome=models.CharField(max_length=200, null=True)
    sexo=models.CharField(max_length=3, null=True)
    altura=models.IntegerField(null=True)
    peso=models.FloatField(null=True)
    nascimento=models.DateField(null=True)
    bairro=models.CharField(max_length=200, null=True)
    cidade=models.CharField(max_length=200, null=True)
    estado=models.CharField(max_length=200, null=True)
    numero=models.IntegerField(null=True)
    nome_arquivo=models.FileField(null=True)
    codigo=models.IntegerField(null=True)
    def __str__(self):
        return self.nome