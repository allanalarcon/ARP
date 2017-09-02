# coding=utf-8
from django import forms
from django.contrib.auth.forms import User
from django.db import models
from Facturas.models import *
from django.contrib.admin import widgets

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
    fecha = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    class Meta:
         model = Factura
         fields = ['razon_social', 'fecha', 'usuario', 'tipo_de_documento', 'tipo_de_gasto', 'secuencia', 'total', 'deducible', 'numero', 'archivo']
         widgets = {
    'fecha': forms.DateInput(attrs={'class':'datepicker'})
}