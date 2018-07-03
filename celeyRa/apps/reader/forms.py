from django import forms
from tasks import tarea
from .models import Archive


class FormLector(forms.ModelForm):

    class Meta:
        model=Archive
        fields=('file',)

    def save(self, commit=True):
        file=super(FormLector, self).save()
        tarea.delay(file.id)
        return file