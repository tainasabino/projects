# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.template import RequestContext, loader
# Create your views here.


def principal(request, template="thamires/home.html"):
    """
    Retorna a páfgina inicial
    :param request:
    :param template:
    :return:
    """
    ola = "Ola Mundo!"
    return render_to_response(template_name=template, context=locals())