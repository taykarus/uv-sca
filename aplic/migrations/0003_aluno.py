# Generated by Django 2.2.19 on 2022-08-13 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('matricula', models.IntegerField(unique=True, verbose_name='Matrícula')),
                ('data_nascimento', models.DateField(blank=True, help_text='Formato DD/MM/AAAA', null=True, verbose_name='Data de Nascimento')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='E-mail')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Curso')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
        ),
    ]
