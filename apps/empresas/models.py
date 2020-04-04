from django.db import models


# Create your models here.
class Empresas(models.Model):
    nome = models.CharField(max_length=100, help_text='nome da empresa')

    def __str__(self):
        return self.nome