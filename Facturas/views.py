from __future__ import unicode_literals
from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,FormView,ListView,UpdateView, DetailView
from .forms import *
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from django.contrib.auth.models import User
from .models import *
from django.views.generic.edit import CreateView

#vistas generales
class Facturas(ListView):
    model = Factura
    template_name = 'facturas.html'
    context_object_name = 'facturas'

class Usuario(ListView):
    model = Usuario
    #fields =['nombre','identificacion','direccion','celular', 'email']
    template_name = 'usuario.html'
    context_object_name = 'usuario'
