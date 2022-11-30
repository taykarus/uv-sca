from rest_framework import serializers
from aplic.models import Curso, Aluno, Disciplina


class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplina
        fields = (
            'id',
            'nome',
            'curso'
        )


class CursoSerializer(serializers.ModelSerializer):
    disciplinas = DisciplinaSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'nome',
            'descricao',
            'imagem',
            'carga_horaria',
            'disciplinas',
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
