# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Words(models.Model):
    englishWord     = models.CharField(max_length=100 , blank=False) # English word  i don't know
    turkishWord    = models.CharField(max_length=200 , blank=False) # Write meaning in turkish
    type            = models.CharField(max_length=100 , blank=False) # Adjective , verb , etc.
    sentence        = models.CharField(max_length=1000 , blank=False) # create one or more sentence

