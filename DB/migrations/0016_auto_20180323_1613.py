# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0015_auto_20180223_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('CI', models.PositiveIntegerField(serialize=False, verbose_name='Carnet de Identidad', primary_key=True)),
                ('edad', models.PositiveSmallIntegerField(verbose_name='Edad', validators=[django.core.validators.MaxValueValidator(130, message='Aun se desconoce si alguien ha sobrepasado los 130')])),
                ('nombreApellidos', models.CharField(max_length=200, verbose_name='Nombre y Apellidos')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('sexo', models.CharField(verbose_name='Sexo', max_length=5, default='F', choices=[('M', 'Masculino'), ('F', 'Femenino')])),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
                ('centroTrabajo', models.CharField(max_length=200, verbose_name='Centro de Trabajo')),
                ('reservaDeQueCuadro', models.CharField(blank=True, max_length=200, verbose_name='Reserva de que Cuadro')),
                ('municipio', models.ForeignKey(to='DB.Municipio')),
                ('organismo', models.ForeignKey(to='DB.Organismo')),
                ('provincia', models.ForeignKey(to='DB.Provincia')),
            ],
            options={
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.RemoveField(
            model_name='autor',
            name='organismo',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='autores',
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='autores',
        ),
        migrations.AlterField(
            model_name='curso',
            name='clasificacion',
            field=models.CharField(verbose_name='Clasificacion', max_length=25, default='Empresarial', choices=[('Administracion Publica', 'Administracion Publica'), ('Empresarial', 'Empresarial')]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='tipo',
            field=models.CharField(verbose_name='Tipo', max_length=25, default='Especialidad', choices=[('Especialidad', 'Especialidad'), ('Diplomado', 'Diplomado')]),
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.AddField(
            model_name='curso',
            name='estudiantes',
            field=models.ManyToManyField(to='DB.Estudiante'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='estudiantes',
            field=models.ManyToManyField(to='DB.Estudiante'),
        ),
    ]
