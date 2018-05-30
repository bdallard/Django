#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

# Classes utilisés durant le projets 
# Toutes les classes héritent de models.Model 
class Client(models.Model):
	#possibilité de def le cclikpi avec CharField(max_length=18) 
	cclikpi = models.IntegerField() 
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	message = models.CharField(max_length=15000)

	#__unicode__(self) pour python2
	def __str__(self): 
		return "{0} {1} {2} : [{3}]".format(self.cclikpi, self.nom, self.prenom, self.message)

"""	
#Client forcément à l'origine d'un message 		
class MessageClient(Client):
	message = models.CharField(max_length=15000)
	
	def __unicode__(self):
		return "{0}".format(self.message) 
"""
