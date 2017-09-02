from django.conf.urls import include, url
from Facturas import views
from Facturas.views import Facturas, Usuario, RegistrarFactura, Eliminar
from django.contrib.auth.decorators import login_required
 
urlpatterns = [
    url(r'^$', login_required(Facturas.as_view()), name="facturas"),
    url(r'^usuario/$',login_required(Usuario.as_view()), name="usuario"), 
    url(r'^registrar/$', login_required(views.RegistrarFactura),name="registrar"),
    url(r'^password/$', login_required(views.change_password), name='change_password'),
    url(r'^editarfactura/(?P<pk>[0-9]+)/$', login_required(views.editar), name='editar'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(Eliminar.as_view()), name='eliminar'),
]