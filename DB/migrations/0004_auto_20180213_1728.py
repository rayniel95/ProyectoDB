# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0003_auto_20171218_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='PalabraClave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('palabra', models.CharField(verbose_name='Palabra', unique=True, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='palabra1',
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='palabra2',
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='palabra3',
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='palabra4',
        ),
        migrations.AlterField(
            model_name='municipio',
            name='nombre',
            field=models.CharField(choices=[('Pinar del Rio', (('ConsolacionDelSur', 'Consolacion del Sur'), ('Guane', 'Guane'), ('LaPalma', 'La Palma'), ('LosPalacios', 'Los Palacios'), ('Mantua', 'Mantua'), ('MinasDeMatahambre', 'Minas de Matahambre'), ('PinarDelRio', 'Pinar del Rio'), ('SanJuanYMartinez', 'San Juan y Martinez'), ('SanLuis', 'San Luis'), ('Sandino', 'Sandino'), ('Vinales', 'Vinales'))), ('Artemisa', (('Alquizar', 'Alquizar'), ('Artemisa', 'Artemisa'), ('Bauta', 'Bauta'), ('Caimito', 'Caimito'), ('Guanajay', 'Guanajay'), ('GuiraDeMelena', 'Guira de Melena'), ('Mariel', 'Mariel'), ('SanAntonioDeLosBanos', 'San Antonio de los Banos'), ('Candelaria', 'Candelaria'), ('SanCristobal', 'San Cristobal'), ('BahiaHonda', 'Bahia Honda'))), ('La Habana', (('ArroyoNaranjo', 'Arroyo Naranjo'), ('Boyeros', 'Boyeros'), ('CentroHabana', 'Centro Habana'), ('Cerro', 'Cerro'), ('Cotorro', 'Cotorro'), ('DiezDeOctubre', 'Diez de Octubre'), ('Guanabacoa', 'Guanabacoa'), ('LaHabanaDelEste', 'La Habana del Este'), ('LaHabanaVieja', 'La Habana Vieja'), ('LaLisa', 'La Lisa'), ('Marianao', 'Marianao'), ('Playa', 'Playa'), ('PlazaDeLaRevolucion', 'Plaza de la Revolucion'), ('Regla', 'Regla'), ('SanMiguelDelPadron', 'San Miguel del Padron'))), ('Mayabeque', (('Batabano', 'Batabano'), ('Bejucal', 'Bejucal'), ('Guines', 'Guines'), ('Jaruco', 'Jaruco'), ('Madruga', 'Madruga'), ('MelenaDelSur', 'Melena del Sur'), ('NuevaPaz', 'Nueva Paz'), ('Quivican', 'Quivican'), ('SanJoseDeLasLajas', 'San Jose de las Lajas'), ('SanNicolas', 'San Nicolas'), ('SantaCruzDelNorte', 'Santa Cruz del Norte'))), ('Matanzas', (('Calimete', 'Calimete'), ('Cardenas', 'Cardenas'), ('CienagaDeZapata', 'Cienaga de Zapata'), ('Colon', 'Colon'), ('JagueyGrande', 'Jaguey Grande'), ('Jovellanos', 'Jovellanos'), ('Limonar', 'Limonar'), ('LosArabos', 'Los Arabos'), ('Marti', 'Marti'), ('Matanzas', 'Matanzas'), ('PedroBetancourt', 'Pedro Betancourt'), ('Perico', 'Perico'), ('UnionDeReyes', 'Union de Reyes'))), ('Cienfuegos', (('Abreus', 'Abreus'), ('AguadaDePasajeros', 'Aguada de Pasajeros'), ('Cienfuegos', 'Cienfuegos'), ('Cruces', 'Cruces'), ('Cumanayagua', 'Cumanayagua'), ('Lajas', 'Lajas'), ('Palmira', 'Palmira'), ('Rodas', 'Rodas'))), ('Villa Clara', (('Caibarien', 'Caibarien'), ('Camajuani', 'Camajuani'), ('Cifuentes', 'Cifuentes'), ('Corralillo', 'Corralillo'), ('Encrucijada', 'Encrucijada'), ('Manicaragua', 'Manicaragua'), ('Placetas', 'Placetas'), ('QuemadoDeGuines', 'Quemado de Guines'), ('Ranchuelo', 'Ranchuelo'), ('SanJuanDeLosRemedios', 'San Juan de los Remedios'), ('SaguaLaGrande', 'Sagua la Grande'), ('SantaClara', 'Santa Clara'), ('SantoDomingo', 'Santo Domingo'))), ('Sancti Spiritus', (('Cabaiguan', 'Cabaiguan'), ('Fomento', 'Fomento'), ('Jatibonico', 'Jatibonico'), ('LaSierpe', 'La Sierpe'), ('SanctiSpiritus', 'Sancti Spiritus'), ('Taguasco', 'Taguasco'), ('Trinidad', 'Trinidad'), ('Yaguajay', 'Yaguajay'))), ('Ciego de Avila', (('Baragua', 'Baragua'), ('Bolivia', 'Bolivia'), ('Chambas', 'Chambas'), ('CiegoDeAvila', 'Ciego de Avila'), ('CiroRedondo', 'Ciro Redondo'), ('Florencia', 'Florencia'), ('Majagua', 'Majagua'), ('Moron', 'Moron'), ('PrimerDeEnero', 'Primero de Enero'), ('Venezuela', 'Venezuela'))), ('Camaguey', (('Camaguey', 'Camaguey'), ('CarlosManuelDeCespedes', 'Carlos M. de Cespedes'), ('Esmeralda', 'Esmeralda'), ('Florida', 'Florida'), ('Guaimaro', 'Guaimaro'), ('Jimaguayu', 'Jimaguayu'), ('Minas', 'Minas'), ('Najasa', 'Najasa'), ('Nuevitas', 'Nuevitas'), ('SantaCruzDelSur', 'Santa Cruz del Sur'), ('Sibanicu', 'Sibanicu'), ('SierraDeCubitas', 'Sierra de Cubitas'), ('Vertientes', 'Vertientes'))), ('Las Tunas', (('Amancio', 'Amancio'), ('Colombia', 'Colombia'), ('JesusMenendez', 'Jesius Menendez'), ('Jobabo', 'Jobabo'), ('Majibacoa', 'Majibacoa'), ('Manati', 'Manati'), ('PuertoPadre', 'Puerto Padre'), ('LasTunas', 'Las Tunas'))), ('Holguin', (('Antilla', 'Antilla'), ('Baguanos', 'Baguanos'), ('Banes', 'Banes'), ('Cacocum', 'Cacocum'), ('CalixtoGarcia', 'Calixto Garcia'), ('Cueto', 'Cueto'), ('FrankPais', 'Frank Pais'), ('Gibara', 'Gibara'), ('Holguin', 'Holguin'), ('Mayari', 'Mayari'), ('Moa', 'Moa'), ('RafaelFreyre', 'Rafael Freyre'), ('SaguaDeTanamo', 'Sagua de Tanamo'), ('Urbano Noris', 'Urbano Noris'))), ('Granma', (('BartolomeMaso', 'Bartolome Maso'), ('Bayamo', 'Bayamo'), ('BueyArriba', 'Buey Arriba'), ('Campechuela', 'Campechuela'), ('CautoCristo', 'Cauto Cristo'), ('Guisa', 'Guisa'), ('Jiguani', 'Jiguani'), ('Manzanillo', 'Manzanillo'), ('MediaLuna', 'Media Luna'), ('Niquero', 'Niquero'), ('Pilon', 'Pilon'), ('RioCauto', 'Rio Cauto'), ('Yara', 'Yara'))), ('Santiago de Cuba', (('Contramaestre', 'Contramaestre'), ('Guama', 'Guama'), ('Mella', 'Mella'), ('PalmaSoriano', 'Palma Soriano'), ('SanLuis', 'San Luis'), ('SantiagoDeCuba', 'Santiago de Cuba'), ('SegundoFrente', 'Segundo Frente'), ('SongoLaMaya', 'Songo-La Maya'), ('TercerFrente', 'Tercer Frente'))), ('Guantanamo', (('Baracoa', 'Baracoa'), ('Caimanera', 'Caimanera'), ('ElSalvador', 'El Salvador'), ('Guantanamo', 'Guantanamo'), ('Imias', 'Imias'), ('Maisi', 'Maisi'), ('ManuelTames', 'Manuel Tames'), ('NicetoPerez', 'Niceto Perez'), ('SanAntonioDelSur', 'San Antonio del Sur'), ('Yateras', 'Yateras'))), ('Isla de la Juventud', (('IslaDeLaJuventud', 'Isla de la Juventud'),))], blank=True, verbose_name='Nombre', max_length=25),
        ),
        migrations.AddField(
            model_name='tesis',
            name='palabras',
            field=models.ManyToManyField(to='DB.PalabraClave'),
        ),
    ]
