from django.forms import *
from django import forms
from .models import *

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
        	'name': 'Name of the task',
        	'planning': 'Planning Time',
        	'estimate': 'Self Estimated Time',
        	'realtime': 'Real Time spent',
        	'risk': 'Risk',
        	'level': 'Level',
            'notes': 'Notes',
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
