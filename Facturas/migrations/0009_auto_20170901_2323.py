# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturas', '0008_auto_20170901_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateField(),
        ),
    ]