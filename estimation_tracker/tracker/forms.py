from django import forms
from tracker.models import Task

LEVEL_CHOICES= [
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard')
]

RISK_CHOICES= [
    ('Not risky', 'Not risky'),
    ('OK', 'OK'),
    ('Risky', 'Risky'),
    ('Very risky', 'Very risky')
]

class TaskForm(forms.ModelForm):
    
    level = forms.CharField(widget=forms.Select(choices=LEVEL_CHOICES))
    risk = forms.CharField(widget=forms.Select(choices=RISK_CHOICES))
    
    class Meta:
        model = Task
        fields = [
            "task_name",
            "planning_time",
            "self_estimated_time",
            "real_time_spent",
            "notes",
            "level",
            "risk",
        ]
