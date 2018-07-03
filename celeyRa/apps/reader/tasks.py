from __future__ import unicode_literals, absolute_import
from django.contrib.auth.models import User
from .models import Archive
from celeyRa import celery_app as app
import xlrd


@app.task
def tarea(f):
    f = Archive.objects.get(pk=f).file.path
    libro = xlrd.open_workbook(f)
    usuario = tuple(libro.sheet_by_index(0).get_rows())
    for filausuario in range(1, len(usuario)):
        user = User()
        for data in range(1, len(usuario[filausuario])):
            user.__setattr__(usuario[0][data].value, usuario[filausuario][data].value)
        user.save()




