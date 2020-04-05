from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresas

# Create your models here.


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome

