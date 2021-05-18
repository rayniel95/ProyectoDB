# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0006_auto_20180223_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincia',
            name='nombre',
            field=models.CharField(verbose_name='Nombre', max_length=25, default='LaHabana', choices=[('PinarDelRio', 'Pinar del Rio'), ('Artemisa', 'Artemisa'), ('LaHabana', 'La Habana'), ('Mayabeque', 'Mayabeque'), ('Matanzas', 'Matanzas'), ('Cienfuegos', 'Cienfuegos'), ('VillaClara', 'Villa Clara'), ('SanctiSpiritus', 'Sancti Spiritus'), ('CiegoDeAvila', 'Ciego de Avila'), ('Camaguey', 'Camaguey'), ('LasTunas', 'Las Tunas'), ('Granma', 'Granma'), ('Holguin', 'Holguin'), ('SantiagoDeCuba', 'Santiago de Cuba'), ('Guantanamo', 'Guantanamo'), ('IslaDeLaJuventud', 'Isla de la Juventud')], unique=True),
        ),
    ]
