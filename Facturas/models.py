from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models,connection
from django.utils import timezone

class Factura(models.Model):
	id_factura = models.AutoField(primary_key=True)
	fecha = models.CharField(max_length=20)
	usuario = models.ForeignKey('Usuario')
	tipo = models.CharField(max_length=20)
	secuencia = models.CharField(max_length=20)
	total = models.FloatField()
	numero = models.CharField(max_length=40)

	def __str__(self):
		return self.numero

class Usuario(models.Model):
	id_usuario = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=40)
	identificacion = models.CharField(max_length=10)
	direccion = models.CharField(max_length=60)
	celular = models.CharField(max_length=10)
	email = models.CharField(max_length=60)

	def __str__(self):
		return self.nombre
