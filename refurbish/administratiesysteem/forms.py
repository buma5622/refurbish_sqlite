from django import forms
from .models import Computer


class RegistratieForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'



