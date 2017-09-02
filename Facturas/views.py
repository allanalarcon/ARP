from __future__ import unicode_literals
from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,FormView,ListView,UpdateView, DetailView
from .forms import *
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from django.contrib.auth.models import User
from .models import *
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .forms import FacturaForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'change_password.html', {'form': form})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

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

def RegistrarFactura(request):
    form = FacturaForm()
    if request.method == "POST":
        form = FacturaForm(request.POST)
        if form.is_valid():
            Factura = form.save(commit=False)
            Factura.save()
            form = FacturaForm()
            return render(request, 'registrarfactura.html', {'form': form, 'mjsexitoso': "Factura guardada"})
    else:
        form = FacturaForm()
    return render(request, 'registrarfactura.html', {'form': form})

def editar(request, pk):
        factura = get_object_or_404(Factura, pk=pk)
        if request.method == "POST":
            form = FacturaForm(request.POST, instance=factura)
            if form.is_valid():
                factura = form.save(commit=False)
                factura.save()
                return render(request, 'registrarfactura.html', {'form': form, 'mjsexitoso': "Factura modificada"})
        else:
            form = FacturaForm(instance=factura)
        return render(request, 'registrarfactura.html', {'form': form})