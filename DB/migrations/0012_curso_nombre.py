# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0011_remove_curso_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre', default='Ejercicios Vespertinos'),
        ),
    ]
