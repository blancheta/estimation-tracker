from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.TextField(blank=False)
    planning_time = models.TimeField(blank=False)
    self_estimated_time = models.TimeField(blank=False)
    real_time_spent = models.TimeField(blank=True, null=True)
    
    notes = models.TextField(blank=True)
    level = models.CharField(max_length=64, blank=True)
    risk = models.CharField(max_length=64, blank=True)
