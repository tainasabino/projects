# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contato(models.Model):
	nome = models.CharField(max_length = 30)
	telefone = models.CharField(max_length = 9)
