# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
# Create your views here.
def principal(request):
	return HttpResponse("Ola mundo")