# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0016_auto_20180323_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.RemoveField(
            model_name='provincia',
            name='id',
        ),
        migrations.AddField(
            model_name='provincia',
            name='codigo',
            field=models.IntegerField(verbose_name='Codigo', default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='municipio',
            field=models.ForeignKey(blank=True, to='DB.Municipio'),
        ),
    ]
