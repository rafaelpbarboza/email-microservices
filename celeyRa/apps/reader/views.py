# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xlrd
import xlsxwriter
from celery import chain
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from tasks import addXlsx, deleteXlsx, sendEmail

# Create your views here.
from .forms import FormLector
from .models import Archive


class Reader (CreateView):
    model = Archive
    form_class = FormLector
    template_name = 'index.html'
    success_url='/'

def crear(request):
    #sendEmail.delay()
    #addXlsx.delay()
    chain(addXlsx.s(), sendEmail.s('prueba','barboza.rafael.p@gmail.com','esto es una prueba','Activos.xlsx'), deleteXlsx.s('Activos.xlsx'))()
    return HttpResponse('hola')




