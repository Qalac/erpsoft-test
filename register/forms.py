from django import forms
from .models import *

class HumanForm(forms.ModelForm):
    name = forms.CharField(max_length=22, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Human
        fields = '__all__'
        
             