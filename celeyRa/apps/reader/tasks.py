from __future__ import unicode_literals, absolute_import
from django.contrib.auth.models import User
from .models import Archive
from celeyRa import celery_app as app
import xlsxwriter
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

@app.task
def addXml():
    cont=0
    workbook = xlsxwriter.Workbook('Activos.xlsx')
    #print("archivo es",workbook.filehandle)
    worksheet = workbook.add_worksheet()
    for p in User.objects.raw('SELECT * FROM auth_user'):
        if  p.is_active:
            worksheet.write(cont, 0, p.id)
            worksheet.write(cont, 1, p.first_name)
            worksheet.write(cont, 2, p.last_name)
            worksheet.write(cont, 3, p.email)
            worksheet.write(cont, 4, p.username)
            cont+=1
    workbook.close()


def sendEmail(subject, to, from_email, msj,file):
    pass
    """
    print("enviando mensaje")
    message(subject,to,from_email,msj,file)
"""



