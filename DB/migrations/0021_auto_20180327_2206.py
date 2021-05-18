# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0020_auto_20180327_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='municipio',
            field=models.ForeignKey(blank=True, to='DB.Municipio', null=True),
        ),
    ]
