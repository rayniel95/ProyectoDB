
# Register your models here.
from django.contrib import admin

from .models import Organismo
from .models import Provincia
from .models import Estudiante
from .models import Curso
from .models import Municipio
from .models import Tesis
from .models import PalabraClave

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('CI', 'nombreApellidos', 'edad', 'email', 'sexo', 'cargo', 'centroTrabajo', 'reservaDeQueCuadro',
                    'provincia', 'organismo', 'municipio',)
    list_per_page = 10

class OrganismoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'siglas',)
    list_per_page = 20

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)
    list_per_page = 10

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'provincia',)
    list_per_page = 10

class PalabraClaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'palabra',)
    list_per_page = 15
    

class TesisAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'ubicacion', 'organismo', 'link', 'Palabras', 'Estudiantes',)
    list_per_page = 10

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'clasificacion', 'edicion',)
    list_per_page = 20

admin.site.register(Organismo, OrganismoAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Tesis, TesisAdmin)
admin.site.register(PalabraClave, PalabraClaveAdmin)

admin.site.site_header = 'Base de datos'




