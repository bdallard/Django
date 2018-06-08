#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import random
import string
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Classes utilisés durant le projets 
# Toutes les classes héritent de models.Model 


class Client(models.Model):
    cclikpi = models.CharField('Client  cclikpi', max_length=20)
    nom = models.CharField('Client  nom', max_length=100)
    prenom = models.CharField('Client  prenom', max_length=100) 
    message = models.CharField('Client message', max_length=10000)


    def __str__(self):
        return self.cclikpi


