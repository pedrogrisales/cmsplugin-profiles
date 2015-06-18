from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import PerfilesPluginModel
from models import PerfilModel
from models import PerfilPluginModel


class PerfilesPlugin(CMSPluginBase):
    model = PerfilesPluginModel
    name = _("Perfiles Plugin")
    render_template = "plugin_perfiles/lista.html"

    def render(self, context, instance, placeholder):
        context['lista'] = PerfilModel.objects.filter(publicar=True,grupo=instance.grupo ).order_by('prioridad')
        # la variable columnas indica el alcho del col-md, 
        # si columnas divide a 12 nos da el 
        # numero real de columnas
        context['columnas'] = str(instance.columnas)
        
        context['size'] = '360x480'
        context['width'] = '360'
        context['height'] = '480'
        if context['columnas'] == '4':
        	context['size'] = '260x347'
	        context['width'] = '263'
	        context['height'] = '347'

        return context


class PerfilPlugin(CMSPluginBase):
    model = PerfilPluginModel
    name = _("Perfil Perfil Plugin")
    render_template = "plugin_perfiles/perfil.html"

    def render(self, context, instance, placeholder):
        context['perfil'] = instance.perfil
        context['size'] = '360x480'
        context['width'] = '360'
        context['height'] = '480'
        return context


plugin_pool.register_plugin(PerfilesPlugin)
plugin_pool.register_plugin(PerfilPlugin)
