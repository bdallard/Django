# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howdy', '0004_auto_20180604_1655'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='client',
            name='cclikpi',
            field=models.CharField(max_length=20, verbose_name='Client  cclikpi'),
        ),
        migrations.AlterField(
            model_name='client',
            name='message',
            field=models.CharField(max_length=10000, verbose_name='Client message'),
        ),
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(max_length=100, verbose_name='Client  nom'),
        ),
        migrations.AlterField(
            model_name='client',
            name='prenom',
            field=models.CharField(max_length=100, verbose_name='Client  prenom'),
        ),
    ]
