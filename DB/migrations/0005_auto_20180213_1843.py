# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0004_auto_20180213_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='palabraclave',
            options={'verbose_name_plural': 'Palabras Claves'},
        ),
        migrations.AlterModelOptions(
            name='tesis',
            options={'verbose_name_plural': 'Tesis'},
        ),
    ]
