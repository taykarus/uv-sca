from rest_framework import serializers
from aplic.models import Curso, Aluno, Disciplina, Professor


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

    @staticmethod
    def validate_carga_horaria(valor):
        if valor >= 20:
            return valor
        raise serializers.ValidationError('Carga Horária inválida')


class AlunoSerializer(serializers.ModelSerializer):
    primeiro_nome = serializers.SerializerMethodField('get_primeiro_nome')

    class Meta:
        model = Aluno
        fields = (
            'id',
            'matricula',
            'data_nascimento',
            'email',
            'nome',
            'curso',
            'primeiro_nome',
        )

    @staticmethod
    def get_primeiro_nome(obj):
        return str(obj.nome).split()[0]


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = (
            'id',
            'nome',
            'titulacao',
            'curso'
        )
