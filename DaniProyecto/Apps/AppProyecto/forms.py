from django import forms
from DaniProyecto.Apps.AppProyecto.models import *

class CuestionarioForm(forms.ModelForm):
    class Meta:
        model=Cuestionario
        fields="__all__"