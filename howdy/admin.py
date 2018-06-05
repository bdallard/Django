#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from import_export import resources
from .models import Client
from .resources import ClientResources
from import_export.admin import ImportExportModelAdmin


# Définition des classes 
	# changer les éléments du form 

# Enregistrer les models ici 

"""
class BookResource(ModelResource):

    class Meta:
        model = Book
	fields = ('cclikpi', 'nom', 'prenom', 'message')

    def for_delete(self, row, instance):
        return self.fields['name'].clean(row) == ''


class BookAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = BookResource
    list_display = ('cclikpi', 'nom', 'prenom', 'message')




admin.site.register(Book, BookAdmin)
"""

@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResources
    list_display = ('cclikpi', 'nom', 'prenom', 'message')


