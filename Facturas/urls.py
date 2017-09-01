from django.conf.urls import include, url
from Facturas import views
from Facturas.views import Facturas, Usuario, RegistrarFactura
from django.contrib.auth.decorators import login_required
 
urlpatterns = [
    url(r'^$', login_required(Facturas.as_view()), name="facturas"),
    url(r'^usuario/$',login_required(Usuario.as_view()), name="usuario"), 
    url(r'^registrar/$', login_required(views.RegistrarFactura),name="registrar"),
    url(r'^password/$', login_required(views.change_password), name='change_password'),
]