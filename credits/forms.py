from django import forms
from .models import Persons

class Personform(forms.ModelForm):

    class Meta:
        model = Persons
        fields = "__all__"