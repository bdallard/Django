#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import random
import string
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Classes utilisés durant le projets 
# Toutes les classes héritent de models.Model 

"""
class Client(models.Model):
	#possibilité de def le cclikpi avec CharField(max_length=18) 
	cclikpi = models.IntegerField(default=0)
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	message = models.CharField(max_length=15000)

	#__unicode__(self) pour python2
	def __str__(self): 
		return "{0} | {1} {2} : {3}".format(self.cclikpi, self.nom, self.prenom, self.message)
"""

class Client(models.Model):
    cclikpi = models.CharField('Client  cclikpi', max_length=20)
    nom = models.CharField('Client  nom', max_length=100)
    prenom = models.CharField('Client  prenom', max_length=100) 
    message = models.CharField('Client message', max_length=10000)


    def __str__(self):
        return self.cclikpi


