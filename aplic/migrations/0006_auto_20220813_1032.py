# Generated by Django 2.2.19 on 2022-08-13 13:32

import aplic.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto'),
        ),
        migrations.AddField(
            model_name='professor',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto'),
        ),
    ]
