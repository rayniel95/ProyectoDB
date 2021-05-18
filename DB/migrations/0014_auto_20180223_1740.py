# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0013_auto_20180223_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesis',
            name='link',
            field=models.URLField(blank=True, verbose_name='Enlace al articulo en Internet'),
        ),
    ]
