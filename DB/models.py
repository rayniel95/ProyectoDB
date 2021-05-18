from django.db import models
from django.core import validators

# Create your models here
from django.utils.html import format_html
from DB import customValidators


class Organismo(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre*')
    siglas = models.CharField(max_length=50, verbose_name='Siglas', blank=True)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    # region Provincias por defecto
    nombreProvincia = (('PinarDelRio', 'Pinar del Rio'),
                       ('Artemisa', 'Artemisa'),
                       ('LaHabana', 'La Habana'),
                       ('Mayabeque', 'Mayabeque'),
                       ('Matanzas', 'Matanzas'),
                       ('Cienfuegos', 'Cienfuegos'),
                       ('VillaClara', 'Villa Clara'),
                       ('SanctiSpiritus', 'Sancti Spiritus'),
                       ('CiegoDeAvila', 'Ciego de Avila'),
                       ('Camaguey', 'Camaguey'),
                       ('LasTunas', 'Las Tunas'),
                       ('Granma', 'Granma'),
                       ('Holguin', 'Holguin'),
                       ('SantiagoDeCuba', 'Santiago de Cuba'),
                       ('Guantanamo', 'Guantanamo'),
                       ('IslaDeLaJuventud', 'Isla de la Juventud'),)
    # endregion
    codigo = models.IntegerField(primary_key=True, verbose_name='Codigo*', default=1)
    nombre = models.CharField(max_length=25, verbose_name='Nombre*', choices=nombreProvincia, default='LaHabana',
                              unique=True)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    class Meta:
        verbose_name_plural = 'Estudiantes'

    sexoAutor = (('M', 'Masculino'), ('F', 'Femenino'))
    maxEdadValidator = validators.MaxValueValidator(130, message='Aun se desconoce si alguien ha sobrepasado los 130')

    CI = models.PositiveIntegerField(primary_key=True, verbose_name='Carnet de Identidad*',
                                     validators=[customValidators.IntLenValidator])

    edad = models.PositiveSmallIntegerField(verbose_name='Edad*', validators=[maxEdadValidator])
    nombreApellidos = models.CharField(max_length=200, verbose_name='Nombre y Apellidos*')
    email = models.EmailField(verbose_name='Email', blank=True)
    sexo = models.CharField(verbose_name='Sexo*', max_length=5, choices=sexoAutor, default='F')
    cargo = models.CharField(verbose_name='Cargo*', max_length=100)
    centroTrabajo = models.CharField(max_length=200, verbose_name='Centro de Trabajo*')
    reservaDeQueCuadro = models.CharField(max_length=200, verbose_name='Reserva de que Cuadro', blank=True)

    organismo = models.ForeignKey(Organismo, verbose_name='Organismo*')
    provincia = models.ForeignKey(Provincia, verbose_name='Provincia*')

    municipio = models.ForeignKey('Municipio', null=True, blank=True)

    def __str__(self):
        return self.nombreApellidos

class Curso(models.Model):
    tipoCurso = (('Especialidad', 'Especialidad'), ('Diplomado', 'Diplomado'),)
    clasificacionCurso = (('Administracion Publica', 'Administracion Publica'), ('Empresarial', 'Empresarial'),)

    tipo = models.CharField(max_length=25, verbose_name='Tipo*', choices=tipoCurso, default='Especialidad')
    clasificacion = models.CharField(max_length=25, verbose_name='Clasificacion*', choices=clasificacionCurso,
                                     default='Empresarial')

    edicion = models.PositiveIntegerField(verbose_name='Edicion*', default=1)
    nombre = models.CharField(max_length=100, verbose_name='Nombre*')

    # todo no esta instanciando la clase datetime.date, esto se da porque parece que este script python no lo ejecuta
    # django lo lee como un script de texto no para ejecutar e interpreta la informacion que esta en el acorde
    #fechaInicio = models.DateField(verbose_name='Fecha de Inicio*')

    estudiantes = models.ManyToManyField(Estudiante, verbose_name='Estudiantes*')

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    # region Municipios por defecto
    nombreMunicipio = (
        ('Pinar del Rio',
         (
            ('ConsolacionDelSur', 'Consolacion del Sur'),
            ('Guane', 'Guane'),
            ('LaPalma', 'La Palma'),
            ('LosPalacios', 'Los Palacios'),
            ('Mantua', 'Mantua'),
            ('MinasDeMatahambre', 'Minas de Matahambre'),
            ('PinarDelRio', 'Pinar del Rio'),
            ('SanJuanYMartinez', 'San Juan y Martinez'),
            ('SanLuis', 'San Luis'),
            ('Sandino', 'Sandino'),
            ('Vinales', 'Vinales'),
         )
        ),
        ('Artemisa',
         (
            ('Alquizar', 'Alquizar'),
            ('Artemisa', 'Artemisa'),
            ('Bauta', 'Bauta'),
            ('Caimito', 'Caimito'),
            ('Guanajay', 'Guanajay'),
            ('GuiraDeMelena', 'Guira de Melena'),
            ('Mariel', 'Mariel'),
            ('SanAntonioDeLosBanos', 'San Antonio de los Banos'),
            ('Candelaria', 'Candelaria'),
            ('SanCristobal', 'San Cristobal'),
            ('BahiaHonda', 'Bahia Honda'),
         )
        ),
        ('La Habana',
         (
            ('ArroyoNaranjo', 'Arroyo Naranjo'),
            ('Boyeros', 'Boyeros'),
            ('CentroHabana', 'Centro Habana'),
            ('Cerro', 'Cerro'),
            ('Cotorro', 'Cotorro'),
            ('DiezDeOctubre', 'Diez de Octubre'),
            ('Guanabacoa', 'Guanabacoa'),
            ('LaHabanaDelEste', 'La Habana del Este'),
            ('LaHabanaVieja', 'La Habana Vieja'),
            ('LaLisa', 'La Lisa'),
            ('Marianao', 'Marianao'),
            ('Playa', 'Playa'),
            ('PlazaDeLaRevolucion', 'Plaza de la Revolucion'),
            ('Regla', 'Regla'),
            ('SanMiguelDelPadron', 'San Miguel del Padron'),
         )
        ),
        ('Mayabeque',
         (
            ('Batabano', 'Batabano'),
            ('Bejucal', 'Bejucal'),
            ('Guines', 'Guines'),
            ('Jaruco', 'Jaruco'),
            ('Madruga', 'Madruga'),
            ('MelenaDelSur', 'Melena del Sur'),
            ('NuevaPaz', 'Nueva Paz'),
            ('Quivican', 'Quivican'),
            ('SanJoseDeLasLajas', 'San Jose de las Lajas'),
            ('SanNicolas', 'San Nicolas'),
            ('SantaCruzDelNorte', 'Santa Cruz del Norte'),
         )
        ),
        ('Matanzas',
         (
            ('Calimete', 'Calimete'),
            ('Cardenas', 'Cardenas'),
            ('CienagaDeZapata', 'Cienaga de Zapata'),
            ('Colon', 'Colon'),
            ('JagueyGrande', 'Jaguey Grande'),
            ('Jovellanos', 'Jovellanos'),
            ('Limonar', 'Limonar'),
            ('LosArabos', 'Los Arabos'),
            ('Marti', 'Marti'),
            ('Matanzas', 'Matanzas'),
            ('PedroBetancourt', 'Pedro Betancourt'),
            ('Perico', 'Perico'),
            ('UnionDeReyes', 'Union de Reyes'),
         )
        ),
        ('Cienfuegos',
         (
            ('Abreus', 'Abreus'),
            ('AguadaDePasajeros', 'Aguada de Pasajeros'),
            ('Cienfuegos', 'Cienfuegos'),
            ('Cruces', 'Cruces'),
            ('Cumanayagua', 'Cumanayagua'),
            ('Lajas', 'Lajas'),
            ('Palmira', 'Palmira'),
            ('Rodas', 'Rodas'),
         )
        ),
        ('Villa Clara',
         (
            ('Caibarien', 'Caibarien'),
            ('Camajuani', 'Camajuani'),
            ('Cifuentes', 'Cifuentes'),
            ('Corralillo', 'Corralillo'),
            ('Encrucijada', 'Encrucijada'),
            ('Manicaragua', 'Manicaragua'),
            ('Placetas', 'Placetas'),
            ('QuemadoDeGuines', 'Quemado de Guines'),
            ('Ranchuelo', 'Ranchuelo'),
            ('SanJuanDeLosRemedios', 'San Juan de los Remedios'),
            ('SaguaLaGrande', 'Sagua la Grande'),
            ('SantaClara', 'Santa Clara'),
            ('SantoDomingo', 'Santo Domingo'),
         )
        ),
        ('Sancti Spiritus',
         (
            ('Cabaiguan', 'Cabaiguan'),
            ('Fomento', 'Fomento'),
            ('Jatibonico', 'Jatibonico'),
            ('LaSierpe', 'La Sierpe'),
            ('SanctiSpiritus', 'Sancti Spiritus'),
            ('Taguasco', 'Taguasco'),
            ('Trinidad', 'Trinidad'),
            ('Yaguajay', 'Yaguajay'),
         )
        ),
        ('Ciego de Avila',
         (
            ('Baragua', 'Baragua'),
            ('Bolivia', 'Bolivia'),
            ('Chambas', 'Chambas'),
            ('CiegoDeAvila', 'Ciego de Avila'),
            ('CiroRedondo', 'Ciro Redondo'),
            ('Florencia', 'Florencia'),
            ('Majagua', 'Majagua'),
            ('Moron', 'Moron'),
            ('PrimerDeEnero', 'Primero de Enero'),
            ('Venezuela', 'Venezuela'),
         )
        ),
        ('Camaguey',
         (
            ('Camaguey', 'Camaguey'),
            ('CarlosManuelDeCespedes', 'Carlos M. de Cespedes'),
            ('Esmeralda', 'Esmeralda'),
            ('Florida', 'Florida'),
            ('Guaimaro', 'Guaimaro'),
            ('Jimaguayu', 'Jimaguayu'),
            ('Minas', 'Minas'),
            ('Najasa', 'Najasa'),
            ('Nuevitas', 'Nuevitas'),
            ('SantaCruzDelSur', 'Santa Cruz del Sur'),
            ('Sibanicu', 'Sibanicu'),
            ('SierraDeCubitas', 'Sierra de Cubitas'),
            ('Vertientes', 'Vertientes'),
         )
        ),
        ('Las Tunas',
         (
            ('Amancio', 'Amancio'),
            ('Colombia', 'Colombia'),
            ('JesusMenendez', 'Jesius Menendez'),
            ('Jobabo', 'Jobabo'),
            ('Majibacoa', 'Majibacoa'),
            ('Manati', 'Manati'),
            ('PuertoPadre', 'Puerto Padre'),
            ('LasTunas', 'Las Tunas'),
         )
        ),
    ('Holguin',
     (
            ('Antilla', 'Antilla'),
            ('Baguanos', 'Baguanos'),
            ('Banes', 'Banes'),
            ('Cacocum', 'Cacocum'),
            ('CalixtoGarcia', 'Calixto Garcia'),
            ('Cueto', 'Cueto'),
            ('FrankPais', 'Frank Pais'),
            ('Gibara', 'Gibara'),
            ('Holguin', 'Holguin'),
            ('Mayari', 'Mayari'),
            ('Moa', 'Moa'),
            ('RafaelFreyre', 'Rafael Freyre'),
            ('SaguaDeTanamo', 'Sagua de Tanamo'),
            ('Urbano Noris', 'Urbano Noris'),
     )
    ),
    ('Granma',
     (
            ('BartolomeMaso', 'Bartolome Maso'),
            ('Bayamo', 'Bayamo'),
            ('BueyArriba', 'Buey Arriba'),
            ('Campechuela', 'Campechuela'),
            ('CautoCristo', 'Cauto Cristo'),
            ('Guisa', 'Guisa'),
            ('Jiguani', 'Jiguani'),
            ('Manzanillo', 'Manzanillo'),
            ('MediaLuna', 'Media Luna'),
            ('Niquero', 'Niquero'),
            ('Pilon', 'Pilon'),
            ('RioCauto', 'Rio Cauto'),
            ('Yara', 'Yara'),
     )
    ),
    ('Santiago de Cuba',
     (
            ('Contramaestre', 'Contramaestre'),
            ('Guama', 'Guama'),
            ('Mella', 'Mella'),
            ('PalmaSoriano', 'Palma Soriano'),
            ('SanLuis', 'San Luis'),
            ('SantiagoDeCuba', 'Santiago de Cuba'),
            ('SegundoFrente', 'Segundo Frente'),
            ('SongoLaMaya', 'Songo-La Maya'),
            ('TercerFrente', 'Tercer Frente'),
     )
    ),
    ('Guantanamo',
     (
            ('Baracoa', 'Baracoa'),
            ('Caimanera', 'Caimanera'),
            ('ElSalvador', 'El Salvador'),
            ('Guantanamo', 'Guantanamo'),
            ('Imias', 'Imias'),
            ('Maisi', 'Maisi'),
            ('ManuelTames', 'Manuel Tames'),
            ('NicetoPerez', 'Niceto Perez'),
            ('SanAntonioDelSur', 'San Antonio del Sur'),
            ('Yateras', 'Yateras'),
     )
    ),
    ('Isla de la Juventud',
     (
            ('IslaDeLaJuventud', 'Isla de la Juventud'),
     )
    ),)
    # endregion
    def __str__(self):
        return self.nombre

    nombre = models.CharField(max_length=25, verbose_name='Nombre*', choices=nombreMunicipio, unique=True)
    provincia = models.ForeignKey(Provincia, verbose_name='Provincia*')

class PalabraClave(models.Model):
    class Meta:
        verbose_name_plural = 'Palabras Clave'

    palabra = models.CharField(max_length=50, verbose_name='Palabra*', unique=True)

    def __str__(self):
        return self.palabra

class Tesis(models.Model):
    class Meta:
        verbose_name_plural = 'Tesis'

    link = models.URLField(verbose_name='Enlace al articulo en Internet', blank=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo*')
    tema = models.TextField(verbose_name='Tema*')
    ubicacion = models.CharField(max_length=100, verbose_name='Ubicacion', blank=True)

    organismo = models.ForeignKey(Organismo, verbose_name='Organismo*')
    estudiantes = models.ManyToManyField(Estudiante, verbose_name='Estudiantes*')

    palabras = models.ManyToManyField(PalabraClave, verbose_name='Palabras claves*')

    def __str__(self):
        return self.titulo

    def Palabras(self):
        html = '<select>'
        for palabra in self.palabras.all():
            html += '<option>' + palabra.__str__() + '</option>'

        html += '</select>'

        return format_html(html)

    def Estudiantes(self):
        html = '<select>'
        for estudiante in self.estudiantes.all():
            html += '<option>' + estudiante.__str__() + '</option>'

        html += '</select>'

        return format_html(html)






