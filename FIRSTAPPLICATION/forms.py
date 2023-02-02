from django import forms
from FIRSTAPPLICATION.models import *

class AddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"