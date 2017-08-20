from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib import admin
from Facturas import views

urlpatterns = [
    #vistas generales
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('seguridad.urls',namespace='seguridad')),
    url(r'^facturas/', include('Facturas.urls',namespace='Facturas')),
]
