# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0019_auto_20180323_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='municipio',
            field=models.ForeignKey(null=True, to='DB.Municipio'),
        ),
    ]
