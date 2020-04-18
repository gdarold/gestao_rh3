
from rest_framework import serializers

from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.api.serializers import Registro_hora_extraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = Registro_hora_extraSerializer(many=True)

    class Meta:
        model = Funcionario
        fields = ['id','nome', 'departamentos', 'empresa', 'user',
                  'total_horas_extra','registrohoraextra_set']



