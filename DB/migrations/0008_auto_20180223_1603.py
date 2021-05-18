# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0007_auto_20180223_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='Organismo',
            new_name='organismo',
        ),
    ]
