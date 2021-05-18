__author__ = 'LsW'

from django.conf.urls import  url

from .views import ConStaticEsp
from .views import ConStaticDip
from .views import ConStaticView
from .views import ConDinamicBusq
from .views import ConStaticAutorNombre
from .views import ConDinamicBusqReset

# se pone el nombre de la app delante del nombre de la url para identificar que el nombre pertenece a la app, en
# caso de existir otra template con el mismo nombre poder identificar esta que pertenece a la app DB
urlpatterns = [
    url(r'^conStaticDip/$', ConStaticDip, name='DB.ConStaticDip'),
    url(r'^conStaticEsp/$', ConStaticEsp, name='DB.ConStaticEsp'),
    url(r'^conStaticView/(?P<authorId>[0-9]+)/$', ConStaticView, name='DB.ConStaticView'),
    url(r'^conDinamicBusq/$', ConDinamicBusq, name='DB.ConDinamicBusq'),
    url(r'^conStaticAuthorName/(?P<courseId>[0-9]+)/$', ConStaticAutorNombre, name='DB.ConStaticAutorNombre'),
    url(r'^conDinamicBusq/reset/$', ConDinamicBusqReset, name='DB.ConDinamicBusqReset'),
]
