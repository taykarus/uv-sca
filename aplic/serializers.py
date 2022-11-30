from rest_framework import serializers
from aplic.models import Curso, Aluno


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


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = (
            'id',
            'matricula',
            'data_nascimento',
            'email',
            'nome',
            'curso'
        )