# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from tasks import addXml

# Create your views here.
from .forms import FormLector
from .models import Archive


class Reader (CreateView):
    model = Archive
    form_class = FormLector
    template_name = 'index.html'
    success_url='/'

def crear(request):
    addXml.delay()
    return HttpResponse('hola')




