from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CategoriaResource(resources.Resource):
    class Meta:
        model = Categoria


class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion',)
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class Meta: 
        models : Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin): 
    search_fields = ['nombres', 'apellidos', 'correo']
    list_display = ('nombres','apellidos','correo', 'fecha_creacion',)
    resource_class = AutorResource


class ProdcutAdminManager(admin.ModelAdmin):    
    exclude = ('slug',)                        

admin.site.register(Post, ProdcutAdminManager)  
admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria)


