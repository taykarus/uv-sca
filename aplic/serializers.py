from rest_framework import serializers
from aplic.models import Curso


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id',
            'nome',
            'descricao',
            'imagem',
            'carga_horaria'
        )
