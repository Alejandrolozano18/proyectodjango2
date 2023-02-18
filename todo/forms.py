from django import forms
from .models import tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = tarea
        fields = ['tarea']