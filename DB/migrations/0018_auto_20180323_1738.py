# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0017_auto_20180323_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='clasificacion',
            field=models.CharField(max_length=25, choices=[('Administracion Publica', 'Administracion Publica'), ('Empresarial', 'Empresarial')], default='Empresarial', verbose_name='Clasificacion*'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='edicion',
            field=models.PositiveIntegerField(default=1, verbose_name='Edicion*'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre*'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='tipo',
            field=models.CharField(max_length=25, choices=[('Especialidad', 'Especialidad'), ('Diplomado', 'Diplomado')], default='Especialidad', verbose_name='Tipo*'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='CI',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Carnet de Identidad*'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='cargo',
            field=models.CharField(max_length=100, verbose_name='Cargo*'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='centroTrabajo',
            field=models.CharField(max_length=200, verbose_name='Centro de Trabajo*'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='edad',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(130, message='Aun se desconoce si alguien ha sobrepasado los 130')], verbose_name='Edad*'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombreApellidos',
            field=models.CharField(max_length=200, verbose_name='Nombre y Apellidos*'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='sexo',
            field=models.CharField(max_length=5, choices=[('M', 'Masculino'), ('F', 'Femenino')], default='F', verbose_name='Sexo*'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='nombre',
            field=models.CharField(max_length=25, choices=[('Pinar del Rio', (('ConsolacionDelSur', 'Consolacion del Sur'), ('Guane', 'Guane'), ('LaPalma', 'La Palma'), ('LosPalacios', 'Los Palacios'), ('Mantua', 'Mantua'), ('MinasDeMatahambre', 'Minas de Matahambre'), ('PinarDelRio', 'Pinar del Rio'), ('SanJuanYMartinez', 'San Juan y Martinez'), ('SanLuis', 'San Luis'), ('Sandino', 'Sandino'), ('Vinales', 'Vinales'))), ('Artemisa', (('Alquizar', 'Alquizar'), ('Artemisa', 'Artemisa'), ('Bauta', 'Bauta'), ('Caimito', 'Caimito'), ('Guanajay', 'Guanajay'), ('GuiraDeMelena', 'Guira de Melena'), ('Mariel', 'Mariel'), ('SanAntonioDeLosBanos', 'San Antonio de los Banos'), ('Candelaria', 'Candelaria'), ('SanCristobal', 'San Cristobal'), ('BahiaHonda', 'Bahia Honda'))), ('La Habana', (('ArroyoNaranjo', 'Arroyo Naranjo'), ('Boyeros', 'Boyeros'), ('CentroHabana', 'Centro Habana'), ('Cerro', 'Cerro'), ('Cotorro', 'Cotorro'), ('DiezDeOctubre', 'Diez de Octubre'), ('Guanabacoa', 'Guanabacoa'), ('LaHabanaDelEste', 'La Habana del Este'), ('LaHabanaVieja', 'La Habana Vieja'), ('LaLisa', 'La Lisa'), ('Marianao', 'Marianao'), ('Playa', 'Playa'), ('PlazaDeLaRevolucion', 'Plaza de la Revolucion'), ('Regla', 'Regla'), ('SanMiguelDelPadron', 'San Miguel del Padron'))), ('Mayabeque', (('Batabano', 'Batabano'), ('Bejucal', 'Bejucal'), ('Guines', 'Guines'), ('Jaruco', 'Jaruco'), ('Madruga', 'Madruga'), ('MelenaDelSur', 'Melena del Sur'), ('NuevaPaz', 'Nueva Paz'), ('Quivican', 'Quivican'), ('SanJoseDeLasLajas', 'San Jose de las Lajas'), ('SanNicolas', 'San Nicolas'), ('SantaCruzDelNorte', 'Santa Cruz del Norte'))), ('Matanzas', (('Calimete', 'Calimete'), ('Cardenas', 'Cardenas'), ('CienagaDeZapata', 'Cienaga de Zapata'), ('Colon', 'Colon'), ('JagueyGrande', 'Jaguey Grande'), ('Jovellanos', 'Jovellanos'), ('Limonar', 'Limonar'), ('LosArabos', 'Los Arabos'), ('Marti', 'Marti'), ('Matanzas', 'Matanzas'), ('PedroBetancourt', 'Pedro Betancourt'), ('Perico', 'Perico'), ('UnionDeReyes', 'Union de Reyes'))), ('Cienfuegos', (('Abreus', 'Abreus'), ('AguadaDePasajeros', 'Aguada de Pasajeros'), ('Cienfuegos', 'Cienfuegos'), ('Cruces', 'Cruces'), ('Cumanayagua', 'Cumanayagua'), ('Lajas', 'Lajas'), ('Palmira', 'Palmira'), ('Rodas', 'Rodas'))), ('Villa Clara', (('Caibarien', 'Caibarien'), ('Camajuani', 'Camajuani'), ('Cifuentes', 'Cifuentes'), ('Corralillo', 'Corralillo'), ('Encrucijada', 'Encrucijada'), ('Manicaragua', 'Manicaragua'), ('Placetas', 'Placetas'), ('QuemadoDeGuines', 'Quemado de Guines'), ('Ranchuelo', 'Ranchuelo'), ('SanJuanDeLosRemedios', 'San Juan de los Remedios'), ('SaguaLaGrande', 'Sagua la Grande'), ('SantaClara', 'Santa Clara'), ('SantoDomingo', 'Santo Domingo'))), ('Sancti Spiritus', (('Cabaiguan', 'Cabaiguan'), ('Fomento', 'Fomento'), ('Jatibonico', 'Jatibonico'), ('LaSierpe', 'La Sierpe'), ('SanctiSpiritus', 'Sancti Spiritus'), ('Taguasco', 'Taguasco'), ('Trinidad', 'Trinidad'), ('Yaguajay', 'Yaguajay'))), ('Ciego de Avila', (('Baragua', 'Baragua'), ('Bolivia', 'Bolivia'), ('Chambas', 'Chambas'), ('CiegoDeAvila', 'Ciego de Avila'), ('CiroRedondo', 'Ciro Redondo'), ('Florencia', 'Florencia'), ('Majagua', 'Majagua'), ('Moron', 'Moron'), ('PrimerDeEnero', 'Primero de Enero'), ('Venezuela', 'Venezuela'))), ('Camaguey', (('Camaguey', 'Camaguey'), ('CarlosManuelDeCespedes', 'Carlos M. de Cespedes'), ('Esmeralda', 'Esmeralda'), ('Florida', 'Florida'), ('Guaimaro', 'Guaimaro'), ('Jimaguayu', 'Jimaguayu'), ('Minas', 'Minas'), ('Najasa', 'Najasa'), ('Nuevitas', 'Nuevitas'), ('SantaCruzDelSur', 'Santa Cruz del Sur'), ('Sibanicu', 'Sibanicu'), ('SierraDeCubitas', 'Sierra de Cubitas'), ('Vertientes', 'Vertientes'))), ('Las Tunas', (('Amancio', 'Amancio'), ('Colombia', 'Colombia'), ('JesusMenendez', 'Jesius Menendez'), ('Jobabo', 'Jobabo'), ('Majibacoa', 'Majibacoa'), ('Manati', 'Manati'), ('PuertoPadre', 'Puerto Padre'), ('LasTunas', 'Las Tunas'))), ('Holguin', (('Antilla', 'Antilla'), ('Baguanos', 'Baguanos'), ('Banes', 'Banes'), ('Cacocum', 'Cacocum'), ('CalixtoGarcia', 'Calixto Garcia'), ('Cueto', 'Cueto'), ('FrankPais', 'Frank Pais'), ('Gibara', 'Gibara'), ('Holguin', 'Holguin'), ('Mayari', 'Mayari'), ('Moa', 'Moa'), ('RafaelFreyre', 'Rafael Freyre'), ('SaguaDeTanamo', 'Sagua de Tanamo'), ('Urbano Noris', 'Urbano Noris'))), ('Granma', (('BartolomeMaso', 'Bartolome Maso'), ('Bayamo', 'Bayamo'), ('BueyArriba', 'Buey Arriba'), ('Campechuela', 'Campechuela'), ('CautoCristo', 'Cauto Cristo'), ('Guisa', 'Guisa'), ('Jiguani', 'Jiguani'), ('Manzanillo', 'Manzanillo'), ('MediaLuna', 'Media Luna'), ('Niquero', 'Niquero'), ('Pilon', 'Pilon'), ('RioCauto', 'Rio Cauto'), ('Yara', 'Yara'))), ('Santiago de Cuba', (('Contramaestre', 'Contramaestre'), ('Guama', 'Guama'), ('Mella', 'Mella'), ('PalmaSoriano', 'Palma Soriano'), ('SanLuis', 'San Luis'), ('SantiagoDeCuba', 'Santiago de Cuba'), ('SegundoFrente', 'Segundo Frente'), ('SongoLaMaya', 'Songo-La Maya'), ('TercerFrente', 'Tercer Frente'))), ('Guantanamo', (('Baracoa', 'Baracoa'), ('Caimanera', 'Caimanera'), ('ElSalvador', 'El Salvador'), ('Guantanamo', 'Guantanamo'), ('Imias', 'Imias'), ('Maisi', 'Maisi'), ('ManuelTames', 'Manuel Tames'), ('NicetoPerez', 'Niceto Perez'), ('SanAntonioDelSur', 'San Antonio del Sur'), ('Yateras', 'Yateras'))), ('Isla de la Juventud', (('IslaDeLaJuventud', 'Isla de la Juventud'),))], verbose_name='Nombre*', unique=True),
        ),
        migrations.AlterField(
            model_name='organismo',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre*'),
        ),
        migrations.AlterField(
            model_name='palabraclave',
            name='palabra',
            field=models.CharField(max_length=50, verbose_name='Palabra*', unique=True),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='codigo',
            field=models.IntegerField(primary_key=True, serialize=False, default=1, verbose_name='Codigo*'),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='nombre',
            field=models.CharField(max_length=25, choices=[('PinarDelRio', 'Pinar del Rio'), ('Artemisa', 'Artemisa'), ('LaHabana', 'La Habana'), ('Mayabeque', 'Mayabeque'), ('Matanzas', 'Matanzas'), ('Cienfuegos', 'Cienfuegos'), ('VillaClara', 'Villa Clara'), ('SanctiSpiritus', 'Sancti Spiritus'), ('CiegoDeAvila', 'Ciego de Avila'), ('Camaguey', 'Camaguey'), ('LasTunas', 'Las Tunas'), ('Granma', 'Granma'), ('Holguin', 'Holguin'), ('SantiagoDeCuba', 'Santiago de Cuba'), ('Guantanamo', 'Guantanamo'), ('IslaDeLaJuventud', 'Isla de la Juventud')], default='LaHabana', verbose_name='Nombre*', unique=True),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='tema',
            field=models.TextField(verbose_name='Tema*'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Titulo*'),
        ),
    ]
