from django.forms import *
from django import forms
from .models import *
from django.utils.translation import gettext_lazy

# form to post request
class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
        'name', 
        'planning', 
        'estimate', 
        'realtime', 
        'risk', 
        'level', 
        'notes', 
        'estimateb_by_calc',
        'correctness'
        ]
        labels = {
        	'name': gettext_lazy('Name of the task'),
        	'planning': gettext_lazy('Planning Time'),
        	'estimate': gettext_lazy('Self Estimated Time'),
        	'realtime': gettext_lazy('Real Time spent'),
        	'risk': gettext_lazy('Risk'),
        	'level': gettext_lazy('Level'),
            'notes': gettext_lazy('Notes'),
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'planning': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'estimate': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'realtime': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'risk': Select(attrs={'class': 'form-control'}),
            'level': Select(attrs={'class': 'form-control'}),
            'notes': TextInput(attrs={'class': 'form-control'}),
            'estimateb_by_calc': HiddenInput(),
            'correctness': HiddenInput(),
        }
