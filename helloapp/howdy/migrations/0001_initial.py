# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-30 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cclikpi', models.IntegerField()),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=15000)),
            ],
        ),
    ]
