# Generated by Django 2.2.19 on 2022-11-30 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0009_curso_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplinas', to='aplic.Curso'),
        ),
    ]
