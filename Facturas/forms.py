# coding=utf-8
from django import forms
from django.contrib.auth.forms import User
from django.db import models
from Facturas.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        labels = {
            'username' : 'Nombre de Usuario',
            'password' : 'Contraseña'
        }

class FacturaForm(forms.ModelForm):
    class Meta:
         model = Factura
         fields = ['razon_social', 'fecha', 'usuario', 'tipo', 'gasto', 'secuencia', 'total', 'deducible', 'numero']