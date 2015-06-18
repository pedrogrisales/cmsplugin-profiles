from django.contrib import admin
from django.utils.translation import ugettext as _
from cms.admin.placeholderadmin import PlaceholderAdmin

from models import PerfilModel
from models import GrupoPerfilModel


class PerfilesAdmin(admin.ModelAdmin):
	list_display = ('prioridad','nombre', 'cargo', 'grupo')
	list_display_links = ('nombre',)
	list_filter = ('grupo', )

admin.site.register(PerfilModel, PerfilesAdmin)
admin.site.register(GrupoPerfilModel)


