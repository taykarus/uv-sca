# Generated by Django 2.2.19 on 2022-08-13 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(verbose_name='Ano')),
                ('semestre', models.IntegerField(verbose_name='Semestre')),
                ('turma', models.CharField(max_length=10, verbose_name='Turma')),
                ('alunos', models.ManyToManyField(to='aplic.Aluno')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.Disciplina')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.Professor')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
    ]