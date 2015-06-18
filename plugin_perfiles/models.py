from django.db import models
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField


class GrupoPerfilModel(models.Model):    
    nombre = models.CharField(max_length=100,blank=False)
    
    def __unicode__(self):
        return self.nombre

    class Meta:        
        verbose_name = "Grupo Perfil"
        verbose_name_plural = "Grupos Perfiles"


class PerfilModel(models.Model):
    prioridad = models.IntegerField(null=True,blank=True)
    nombre = models.CharField(max_length=100,blank=False)
    cargo = models.CharField(max_length=100,blank=False)
    publicar = models.BooleanField(default=True)
    imagen = FilerImageField(blank=False)
    grupo = models.ForeignKey(GrupoPerfilModel, null=True, blank=False, default=None)

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ['prioridad'] 
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"


class PerfilesPluginModel(CMSPlugin):
    PLUGIN_COLUMNAS = (
        (4, "Cuatro columnas"),
        (3, "Tres columnas"),
    )    
    columnas = models.IntegerField(choices=PLUGIN_COLUMNAS, default=1)
    grupo = models.ForeignKey(GrupoPerfilModel, null=True, blank=False, default=None)
    

class PerfilPluginModel(CMSPlugin):        
    perfil = models.ForeignKey(PerfilModel)

