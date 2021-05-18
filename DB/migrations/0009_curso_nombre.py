# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0008_auto_20180223_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='nombre',
            field=models.CharField(verbose_name='Nombre', max_length=100, default=1),
            preserve_default=False,
        ),
    ]
