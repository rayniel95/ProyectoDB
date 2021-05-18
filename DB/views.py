import os
import pickle
import io
from django import shortcuts
from django.contrib.admin.sites import site
from DB.code import Consul

# Create your views here.

def ConStaticDip(request):
    if site.has_permission(request):
        query = Consul.DipConsul()
        return shortcuts.render_to_response(os.path.join('DB', 'TemplateConStaticDiplomado.html'),
                                            {'diplomados': query})
    raise shortcuts.Http404()

def ConStaticEsp(request):
    if site.has_permission(request):
        query = Consul.EspConsul()
        return shortcuts.render_to_response(os.path.join('DB', 'TemplateConStaticEspecialidad.html'),
                                            {'especialidades': query})
    raise shortcuts.Http404()

def ConStaticView(request, authorId):
    if site.has_permission(request):
        query = Consul.AuthorInfo(authorId)
        return shortcuts.render_to_response(os.path.join('DB', 'TemplateConStaticView.html'), {'autor': query})
    raise shortcuts.Http404()

def ConStaticAutorNombre(request, courseId):
    if site.has_permission(request):
        query = Consul.StaticViewConsul(courseId)
        return shortcuts.render_to_response(os.path.join('DB', 'TemplateConStaticAutorNombre.html'), {'autores': query})
    raise shortcuts.Http404()

def ConDinamicBusq(request):
    if site.has_permission(request):

        if 'raio' in request.GET:
            # se le pregunta al request que usuario es y en dependencia se carga el pickle de ese usuario
            radioId = request.GET['raio']
            busq = request.GET['busqeda']

            if busq == '':
                 return shortcuts.render_to_response(os.path.join('DB', 'TemplateConDinamicBuscador.html'))

            try:
                # si no existe se crea
                # todo hay que cerrar el file al acabar
                file = open(request.user.__str__(), 'rb') # se crea solo si se abre en modo de escritura
            except:
                # el file no se puede abrir por alguna razon se retorna una consulta vacia o que diga que hubo un error
                # y que llame al administrador
                print('error en abrir el file')
                pass

            try:
                result = pickle.load(file)
                print('se cargo la estructura')
            except:
                # se hace algo parecido a lo de arriba, si no se pudo cargar es porque el archivo aunque existe, esta
                # vacio, en ese caso lo que se haria seria llenarlo con alguna especie de flag que me indique que debo
                # realizar una consulta nueva y no cargar lo que esta y realizar una subconsulta
                print('el file estaba vacio')
                result = (None, 'new')


            try:
                file.close()
                print('se cerro el file')
            except:
                pass

            if result[1] == 'new':

                file = open(request.user.__str__(), 'wb')

                query = Consul.DinamicBusqConsul(radioId, busq)

                estructura = (query, 'sub')

                pickle.dump(estructura, file)

                print('se realizo una consulta nueva, y se cargo la estructura al file')

            else:
                # result es el resultado de una subconsulta

                file = open(request.user.__str__(), 'wb')

                query = Consul.SubDinamicBusqConsul(radioId, busq, result[0])

                estructura = (query, 'sub')

                pickle.dump(estructura, file)

                print('se realizo una subconsulta y se guardo la estructura')

            try:
                file.close()
                print('se cerro el file')
            except:
                pass

            return shortcuts.render_to_response(os.path.join('DB', 'TemplateConDinamicBuscador.html'),
                                            {'resultado': query, 'count': query.count()})

        try:
            file = open(request.user.__str__(), 'rb')

            estructura = pickle.load(file)

            file.close()

            return shortcuts.render_to_response(os.path.join('DB', 'TemplateConDinamicBuscador.html'),
                                                {'resultado': estructura[0], 'count': estructura[0].count()})
        except:
            return shortcuts.render_to_response(os.path.join('DB', 'TemplateConDinamicBuscador.html'))

    raise shortcuts.Http404()

# ideal ver como poner el boton de restablecer en el mismo view del boton enviar consulta
def ConDinamicBusqReset(request):
     if site.has_permission(request):

        try:
            print('se hizo reset')
            file = open(request.user.__str__(), 'wb')
            file.close()
        except:
            pass

        return shortcuts.render_to_response(os.path.join('DB', 'TemplateConDinamicBuscador.html'))