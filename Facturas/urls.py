from django.conf.urls import include, url
from Facturas import views
from Facturas.views import Facturas, Usuario
from django.contrib.auth.decorators import login_required
 
urlpatterns = [
    url(r'^$', login_required(Facturas.as_view()), name="facturas"),
    url(r'^usuario/$',login_required(Usuario.as_view()), name="usuario"),
]
