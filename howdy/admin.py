#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from import_export import resources
from .models import Client
from .resources import ClientResources
from import_export.admin import ImportExportModelAdmin



# Enregistrer les models ici 

@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResources
    list_display = ('cclikpi', 'nom', 'prenom', 'message')


