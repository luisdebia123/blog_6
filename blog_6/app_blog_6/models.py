from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.forms import modelformset_factory
from django.shortcuts import reverse   
import uuid                            
from django.utils.text import slugify  
from django.db.models.signals import pre_save  

# Create your models here.

class Categoria(models.Model):
    id_categorias = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null=False,blank=False )
    estado = models.BooleanField('Categoria Activada/Categoria no activada', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add=True)

    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categoria')
    
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombres = models.CharField ('Nombres de Autor', max_length=255, null= False, blank = False)
    apellidos = models.CharField ('Apellidos de Autor', max_length=255, null= False, blank = False)
    facebook = models.URLField('facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagran', null=True, blank=True)
    wed = models.URLField('Wed', null=True, blank=True)
    correo =  models.EmailField('Correo Electronico', blank = False, null = False)
    estado = models.BooleanField('Autor activo/ No Activo', default = True)
    fecha_creacion = models.DateField('fecha_creacion', auto_now= False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural =  'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)

class Post(models.Model):
    id_post = models.AutoField(primary_key=True )
    titulo = models.CharField('Titulo', max_length=90, blank = False, null=False)
    descripcion = models.CharField('Desceipción', max_length=110, blank = False, null=False)
    contenido = RichTextField('Contenido')
    image = models.URLField(max_length=255, blank = False, null=False)
    autor = models.ForeignKey('Autor', on_delete = models.CASCADE )
    categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateTimeField('Fecha de Creación',auto_now=False, auto_now_add=True)
    slug = models.SlugField(null=False, blank=False, unique=True)



    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = ('Posts')

    def __str__(self):  
        return self.slug

def set_slug(sender, instance, *args, **kwargs):  
    if instance.slug:
        return 

    id = str (uuid.uuid4()) 
    instance.slug = slugify('{}-{}'.format(instance.autor, id[:8])) 

pre_save.connect(set_slug, sender = Post) 

