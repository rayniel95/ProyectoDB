# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0009_curso_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=100, default='Ejercicios Vespertinos', verbose_name='Nombre'),
        ),
    ]
