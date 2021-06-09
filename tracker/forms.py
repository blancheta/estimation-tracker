from django.forms import *
from django import forms
from .models import *
from .utils import *

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
            'correctness',
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

    def save (self, *args,commit=True):
        #------------------------------------------------------------------------------------#
        # save form data with commit=False. If commit= False, data haven't add in database
        #------------------------------------------------------------------------------------#
        instance = super(CreateTaskForm, self).save(*args, commit=False)
        if self.is_valid():
            # calculate estimation & correctness and save estimation and correctness in instance
            instance.estimateb_by_calc = calc_estimation_time(self.cleaned_data["estimate"], self.cleaned_data["realtime"])
            instance.correctness = calc_correctness(self.cleaned_data["estimate"], self.cleaned_data["realtime"])
            if commit:
                instance.save()
        return instance