# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0018_auto_20180323_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='estudiantes',
            field=models.ManyToManyField(to='DB.Estudiante', verbose_name='Estudiantes*'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='organismo',
            field=models.ForeignKey(to='DB.Organismo', verbose_name='Organismo*'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='provincia',
            field=models.ForeignKey(to='DB.Provincia', verbose_name='Provincia*'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='provincia',
            field=models.ForeignKey(to='DB.Provincia', verbose_name='Provincia*'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='estudiantes',
            field=models.ManyToManyField(to='DB.Estudiante', verbose_name='Estudiantes*'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='organismo',
            field=models.ForeignKey(to='DB.Organismo', verbose_name='Organismo*'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='palabras',
            field=models.ManyToManyField(to='DB.PalabraClave', verbose_name='Palabras claves*'),
        ),
    ]
