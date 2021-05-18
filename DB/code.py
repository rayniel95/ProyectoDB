from .models import Tesis
from .models import Curso
from .models import Estudiante


class Consul:
    @staticmethod
    def DipConsul():
        return Curso.objects.filter(tipo='Diplomado')

    @staticmethod
    def AuthorInfo(id):
        return Estudiante.objects.get(pk=id)

    @staticmethod
    def EspConsul():
        return Curso.objects.filter(tipo='Especialidad')

    @staticmethod
    def StaticViewConsul(id):
        '''
        :param id: string con el valor del id del elemento de la tabla
        :return: un objeto tipo QuerySet
        '''
        return Curso.objects.get(pk=id).estudiantes.all()

    @staticmethod
    def DinamicBusqConsul(idradio, textbox):
        '''
        Realiza una consulta basada en los parametros seleccionados en la app
        :param idradio: tipo string, se pasa el value de un radio button de la app para saber la opcion
                        seleccionada
        :param textbox: tipo string, se pasa el texto de un textbox con lo que se desea buscar
        :return: un objeto de tipo QuerySet de Django, con los elementos de la consulta realizada
        '''
        if idradio == 'byOrganism':
            return FiltTesisPorNombreOrganismo(textbox)

        elif idradio == 'byProvince':
            return FiltTesisPorNombreProvincia(textbox)

        elif idradio == 'byWorkCenter':
            return FiltTesisPorCentroTrabajo(textbox)

        elif idradio == 'byCargo':
            return FiltTesisPorCargo(textbox)

        elif idradio == 'byWord':
            return FiltTesisPorPalabras(textbox.strip().split(','))

        else: # se filtro por autor por defecto
            return FiltTesisPorNombreAutor(textbox)

    @staticmethod
    def SubDinamicBusqConsul(idradio, textbox, query):
        if idradio == 'byOrganism':
            return SubFiltTesisPorNombreOrganismo(textbox, query)

        elif idradio == 'byProvince':
            return SubFiltTesisPorNombreProvincia(textbox, query)

        elif idradio == 'byWorkCenter':
            return SubFiltTesisPorCentroTrabajo(textbox, query)

        elif idradio == 'byCargo':
            return SubFiltTesisPorCargo(textbox, query)

        elif idradio == 'byWord':
            return SubFiltTesisPorPalabras(textbox.strip().split(','), query)

        else: # se filtro por autor por defecto
            return SubFiltTesisPorNombreAutor(textbox, query)

def FiltTesisPorNombreOrganismo(organism):
    '''
    Reliza la consulta de las tesis filtrando por el organismo, o sea, dado el organismo, devuelve las tesis
    que fueron realizadas para el mismo
    :param organism: un string, el organismo por el cual se va a filtrar, se usa contains
    :return: el QuerySet de Django conteniendo las tesis que cumplen con la consulta pedida
    '''
    return Tesis.objects.filter(organismo__nombre__icontains=organism)

def FiltTesisPorNombreAutor(autor):
    '''
    Realiza una consultas sobre las tesis buscando por autor, o sea, para aquellos autores que tengan nombre que
    esten contenidos en el parametro, devuelve las tesis en la que se han visto involucrados
    :param autor: string con el nombre del autor a buscar
    :return: un objeto tipo QuerySet de Django con las tesis encontradas
    '''
    return Tesis.objects.filter(estudiantes__nombreApellidos__icontains=autor)

def FiltTesisPorNombreProvincia(prov):
    return Tesis.objects.filter(estudiantes__provincia__nombre__icontains=prov)

def FiltTesisPorCentroTrabajo(centro):
    return Tesis.objects.filter(estudiantes__centroTrabajo__icontains=centro)

def FiltTesisPorCargo(cargo):
    return Tesis.objects.filter(estudiantes__cargo__icontains=cargo)

def FiltTesisPorPalabras(palabras):

    query = Tesis.objects.filter(palabras__palabra__icontains=palabras[0])

    for indice in range(1, len(palabras)):
        query = query.filter(palabras__palabra__icontains=palabras[indice])

    return query

def SubFiltTesisPorNombreOrganismo(organism, query):
    return query.filter(organismo__nombre__icontains=organism).distinct()

def SubFiltTesisPorNombreAutor(autor, query):
    return query.filter(estudiantes__nombreApellidos__icontains=autor).distinct()

def SubFiltTesisPorNombreProvincia(prov, query):
    return query.filter(estudiantes__provincia__nombre__icontains=prov).distinct()

def SubFiltTesisPorCentroTrabajo(centro, query):
    return query.filter(estudiantes__centroTrabajo__icontains=centro).distinct()

def SubFiltTesisPorCargo(cargo, query):
    return query.filter(estudiantes__cargo__icontains=cargo).distinct()

def SubFiltTesisPorPalabras(palabras, query):

    result = query.filter(palabras__palabra__icontains=palabras[0])

    for indice in range(1, len(palabras)):
        result = result.filter(palabras__palabra__icontains=palabras[indice])

    return result.distinct()

