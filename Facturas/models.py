from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models,connection
from django.utils import timezone

class Factura(models.Model):
	id_factura = models.AutoField(primary_key=True)
	razon_social = models.CharField(max_length=40)
	fecha = models.DateField()
	usuario = models.ForeignKey('Usuario')
	tipo_de_documento = models.CharField(max_length=20)
	tipo_de_gasto = models.CharField(max_length=40)
	secuencia = models.CharField(max_length=20)
	total = models.FloatField()
	deducible = models.FloatField()
	numero = models.CharField(max_length=40)
	archivo = models.CharField(max_length=100, default="Sin archivo")

	def __str__(self):
		return self.numero

	class Meta:
		ordering = ["-fecha"]

class Usuario(models.Model):
	id_usuario = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=40)
	identificacion = models.CharField(max_length=10)
	direccion = models.CharField(max_length=60)
	celular = models.CharField(max_length=10)
	email = models.CharField(max_length=60)

	def __str__(self):
		return self.nombre
