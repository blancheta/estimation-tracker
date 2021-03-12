from django.forms import ModelForm
from .models import *

class DataForm (ModelForm):
    class Meta:
        model=Table
        fields = '__all__'