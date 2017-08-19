from __future__ import unicode_literals
from django.contrib import admin
from .models import *

class FacturasAdmin(admin.ModelAdmin):
	list_display=('id_factura','fecha','usuario','tipo','secuencia','total','numero')
	list_filter=("id_factura",)
	search_fields=("fecha","total","tipo",)

admin.site.register(Usuario)
admin.site.register(Factura,FacturasAdmin)
