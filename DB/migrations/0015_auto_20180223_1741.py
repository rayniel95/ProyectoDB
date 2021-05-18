# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0014_auto_20180223_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesis',
            name='ubicacion',
            field=models.CharField(max_length=100, verbose_name='Ubicacion', blank=True),
        ),
    ]
