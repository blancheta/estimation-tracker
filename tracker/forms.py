from django.forms import ModelForm
from .models import *


class DataForm(ModelForm):
    class Meta:
        model = Task
        fields = {'name', 'planning', 'estimate', 'realtime', 'risk', 'level', 'notes'}
