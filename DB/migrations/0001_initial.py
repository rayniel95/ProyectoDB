# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('CI', models.PositiveIntegerField(verbose_name='Carnet de Identidad', primary_key=True, serialize=False)),
                ('edad', models.PositiveSmallIntegerField(verbose_name='Edad', validators=[django.core.validators.MaxValueValidator(130, message='Aun se desconoce si alguien ha sobrepasado los 130')])),
                ('nombreApellidos', models.CharField(verbose_name='Nombre y Apellidos', max_length=200)),
                ('email', models.EmailField(verbose_name='Email', blank=True, max_length=254)),
                ('sexo', models.CharField(verbose_name='Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')], default='F', max_length=5)),
                ('cargo', models.CharField(verbose_name='Cargo', max_length=100)),
                ('centroTrabajo', models.CharField(verbose_name='Centro de Trabajo', max_length=200)),
                ('reservaDeQueCuadro', models.CharField(verbose_name='Reserva de que Cuadro', blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tipo', models.CharField(verbose_name='Tipo', choices=[('Especialidad', 'Especialidad'), ('Doctorado', 'Doctorado')], default='Especialidad', max_length=25)),
                ('clasificacion', models.CharField(verbose_name='Clasificacion', choices=[('Relaciones Publicas', 'Relaciones Publicas'), ('Empresarial', 'Empresarial')], default='Empresarial', max_length=25)),
                ('edicion', models.PositiveIntegerField(verbose_name='Edicion', default=1)),
                ('autores', models.ManyToManyField(to='DB.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(verbose_name='Nombre', choices=[('PinarDelRio', (('ConsolacionDelSur', 'Consolacion del Sur'), ('Guane', 'Guane'), ('LaPalma', 'La Palma'), ('LosPalacios', 'Los Palacios'), ('Mantua', 'Mantua'), ('MinasDeMatahambre', 'Minas de Matahambre'), ('PinarDelRio', 'Pinar del Rio'), ('SanJuanYMartinez', 'San Juan y Martinez'), ('SanLuis', 'San Luis'), ('Sandino', 'Sandino'), ('Vinales', 'Vinales'))), ('Artemisa', (('Alquizar', 'Alquizar'), ('Artemisa', 'Artemisa'), ('Bauta', 'Bauta'), ('Caimito', 'Caimito'), ('Guanajay', 'Guanajay'), ('GuiraDeMelena', 'Guira de Melena'), ('Mariel', 'Mariel'), ('SanAntonioDeLosBanos', 'San Antonio de los Banos'), ('Candelaria', 'Candelaria'), ('SanCristobal', 'San Cristobal'), ('BahiaHonda', 'Bahia Honda'))), ('LaHabana', (('ArroyoNaranjo', 'Arroyo Naranjo'), ('Boyeros', 'Boyeros'), ('CentroHabana', 'Centro Habana'), ('Cerro', 'Cerro'), ('Cotorro', 'Cotorro'), ('DiezDeOctubre', 'Diez de Octubre'), ('Guanabacoa', 'Guanabacoa'), ('LaHabanaDelEste', 'La Habana del Este'), ('LaHabanaVieja', 'La Habana Vieja'), ('LaLisa', 'La Lisa'), ('Marianao', 'Marianao'), ('Playa', 'Playa'), ('PlazaDeLaRevolucion', 'Plaza de la Revolucion'), ('Regla', 'Regla'), ('SanMiguelDelPadron', 'San Miguel del Padron'))), ('Mayabeque', (('Batabano', 'Batabano'), ('Bejucal', 'Bejucal'), ('Guines', 'Guines'), ('Jaruco', 'Jaruco'), ('Madruga', 'Madruga'), ('MelenaDelSur', 'Melena del Sur'), ('NuevaPaz', 'Nueva Paz'), ('Quivican', 'Quivican'), ('SanJoseDeLasLajas', 'San Jose de las Lajas'), ('SanNicolas', 'San Nicolas'), ('SantaCruzDelNorte', 'Santa Cruz del Norte'))), ('Matanzas', (('Calimete', 'Calimete'), ('Cardenas', 'Cardenas'), ('CienagaDeZapata', 'Cienaga de Zapata'), ('Colon', 'Colon'), ('JagueyGrande', 'Jaguey Grande'), ('Jovellanos', 'Jovellanos'), ('Limonar', 'Limonar'), ('LosArabos', 'Los Arabos'), ('Marti', 'Marti'), ('Matanzas', 'Matanzas'), ('PedroBetancourt', 'Pedro Betancourt'), ('Perico', 'Perico'), ('UnionDeReyes', 'Union de Reyes'))), ('Cienfuegos', (('Abreus', 'Abreus'), ('AguadaDePasajeros', 'Aguada de Pasajeros'), ('Cienfuegos', 'Cienfuegos'), ('Cruces', 'Cruces'), ('Cumanayagua', 'Cumanayagua'), ('Lajas', 'Lajas'), ('Palmira', 'Palmira'), ('Rodas', 'Rodas'))), ('VillaClara', (('Caibarien', 'Caibarien'), ('Camajuani', 'Camajuani'), ('Cifuentes', 'Cifuentes'), ('Corralillo', 'Corralillo'), ('Encrucijada', 'Encrucijada'), ('Manicaragua', 'Manicaragua'), ('Placetas', 'Placetas'), ('QuemadoDeGuines', 'Quemado de Guines'), ('Ranchuelo', 'Ranchuelo'), ('SanJuanDeLosRemedios', 'San Juan de los Remedios'), ('SaguaLaGrande', 'Sagua la Grande'), ('SantaClara', 'Santa Clara'), ('SantoDomingo', 'Santo Domingo'))), ('SanctiSpiritus', (('Cabaiguan', 'Cabaiguan'), ('Fomento', 'Fomento'), ('Jatibonico', 'Jatibonico'), ('LaSierpe', 'La Sierpe'), ('SanctiSpiritus', 'Sancti Spiritus'), ('Taguasco', 'Taguasco'), ('Trinidad', 'Trinidad'), ('Yaguajay', 'Yaguajay'))), ('CiegoDeAvila', (('Baragua', 'Baragua'), ('Bolivia', 'Bolivia'), ('Chambas', 'Chambas'), ('CiegoDeAvila', 'Ciego de Avila'), ('CiroRedondo', 'Ciro Redondo'), ('Florencia', 'Florencia'), ('Majagua', 'Majagua'), ('Moron', 'Moron'), ('PrimerDeEnero', 'Primero de Enero'), ('Venezuela', 'Venezuela'))), ('Camaguey', (('Camaguey', 'Camaguey'), ('CarlosManuelDeCespedes', 'Carlos M. de Cespedes'), ('Esmeralda', 'Esmeralda'), ('Florida', 'Florida'), ('Guaimaro', 'Guaimaro'), ('Jimaguayu', 'Jimaguayu'), ('Minas', 'Minas'), ('Najasa', 'Najasa'), ('Nuevitas', 'Nuevitas'), ('SantaCruzDelSur', 'Santa Cruz del Sur'), ('Sibanicu', 'Sibanicu'), ('SierraDeCubitas', 'Sierra de Cubitas'), ('Vertientes', 'Vertientes'))), ('LasTunas', (('Amancio', 'Amancio'), ('Colombia', 'Colombia'), ('JesusMenendez', 'Jesius Menendez'), ('Jobabo', 'Jobabo'), ('Majibacoa', 'Majibacoa'), ('Manati', 'Manati'), ('PuertoPadre', 'Puerto Padre'), ('LasTunas', 'Las Tunas'))), ('Holguin', (('Antilla', 'Antilla'), ('Baguanos', 'Baguanos'), ('Banes', 'Banes'), ('Cacocum', 'Cacocum'), ('CalixtoGarcia', 'Calixto Garcia'), ('Cueto', 'Cueto'), ('FrankPais', 'Frank Pais'), ('Gibara', 'Gibara'), ('Holguin', 'Holguin'), ('Mayari', 'Mayari'), ('Moa', 'Moa'), ('RafaelFreyre', 'Rafael Freyre'), ('SaguaDeTanamo', 'Sagua de Tanamo'), ('Urbano Noris', 'Urbano Noris'))), ('Granma', (('BartolomeMaso', 'Bartolome Maso'), ('Bayamo', 'Bayamo'), ('BueyArriba', 'Buey Arriba'), ('Campechuela', 'Campechuela'), ('CautoCristo', 'Cauto Cristo'), ('Guisa', 'Guisa'), ('Jiguani', 'Jiguani'), ('Manzanillo', 'Manzanillo'), ('MediaLuna', 'Media Luna'), ('Niquero', 'Niquero'), ('Pilon', 'Pilon'), ('RioCauto', 'Rio Cauto'), ('Yara', 'Yara'))), ('SantiagoDeCuba', (('Contramaestre', 'Contramaestre'), ('Guama', 'Guama'), ('Mella', 'Mella'), ('PalmaSoriano', 'Palma Soriano'), ('SanLuis', 'San Luis'), ('SantiagoDeCuba', 'Santiago de Cuba'), ('SegundoFrente', 'Segundo Frente'), ('SongoLaMaya', 'Songo-La Maya'), ('TercerFrente', 'Tercer Frente'))), ('Guantanamo', (('Baracoa', 'Baracoa'), ('Caimanera', 'Caimanera'), ('ElSalvador', 'El Salvador'), ('Guantanamo', 'Guantanamo'), ('Imias', 'Imias'), ('Maisi', 'Maisi'), ('ManuelTames', 'Manuel Tames'), ('NicetoPerez', 'Niceto Perez'), ('SanAntonioDelSur', 'San Antonio del Sur'), ('Yateras', 'Yateras'))), ('IslaDeLaJuventud', ((),))], blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Organismo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(verbose_name='Nombre', max_length=200)),
                ('siglas', models.CharField(verbose_name='Siglas', blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(verbose_name='Nombre', choices=[('PinarDelRio', 'Pinar del Rio'), ('Artemisa', 'Artemisa'), ('LaHabana', 'La Habana'), ('Mayabeque', 'Mayabeque'), ('Matanzas', 'Matanzas'), ('Cienfuegos', 'Cienfuegos'), ('VillaClara', 'Villa Clara'), ('SanctiSpiritus', 'Sancti Spiritus'), ('CiegoDeAvila', 'Ciego de Avila'), ('Camaguey', 'Camaguey'), ('LasTunas', 'Las Tunas'), ('Granma', 'Granma'), ('Holguin', 'Holguin'), ('SantiagoDeCuba', 'Santiago de Cuba'), ('Guantanamo', 'Guantanamo'), ('IslaDeLaJuventud', 'Isla de la Juventud')], default='LaHabana', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('link', models.URLField(verbose_name='Enlace al articulo en Internet', blank=True)),
                ('titulo', models.CharField(verbose_name='Titulo', max_length=100)),
                ('tema', models.TextField(verbose_name='Tema')),
                ('ubicacion', models.CharField(verbose_name='Ubicacion', blank=True, max_length=100)),
                ('palabra1', models.CharField(verbose_name='Primera Palabra Clave', blank=True, max_length=50)),
                ('palabra2', models.CharField(verbose_name='Segunda Palabra Clave', blank=True, max_length=50)),
                ('palabra3', models.CharField(verbose_name='Tercera Palabra Clave', blank=True, max_length=50)),
                ('palabra4', models.CharField(verbose_name='Cuarta Palabra Clave', blank=True, max_length=50)),
                ('autores', models.ManyToManyField(to='DB.Autor')),
                ('organismo', models.ForeignKey(to='DB.Organismo')),
            ],
        ),
        migrations.AddField(
            model_name='municipio',
            name='provincia',
            field=models.ForeignKey(to='DB.Provincia'),
        ),
        migrations.AddField(
            model_name='autor',
            name='Organismo',
            field=models.ForeignKey(to='DB.Organismo'),
        ),
        migrations.AddField(
            model_name='autor',
            name='provincia',
            field=models.ForeignKey(to='DB.Provincia'),
        ),
    ]
