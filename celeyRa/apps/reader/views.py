# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView

# Create your views here.
from .forms import FormLector
from .models import Archive


class Reader (CreateView):
    model = Archive
    form_class = FormLector
    template_name = 'index.html'
    success_url='/'





