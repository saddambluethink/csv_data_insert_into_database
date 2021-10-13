from django import forms
from django.forms import fields

# for csv 
from .models import csvfile

class csvform(forms.ModelForm):
    class Meta:
        model=csvfile
        fields =("csv_file", )

