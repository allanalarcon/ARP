# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturas', '0006_factura_archivo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura',
            options={'ordering': ['-fecha']},
        ),
        migrations.AlterField(
            model_name='factura',
            name='archivo',
            field=models.CharField(max_length=100),
        ),
    ]
