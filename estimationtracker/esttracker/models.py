# Name of the task: String

# Planning Time: HH:MM:SS, Time needed to plan work for this task

# Self Estimated Time: HH:MM:SS, Time estimation given by the developer

# Real Time spent HH:MM:SS, Real time spent to complete the task (To add when the task is completed)

# Level: String, Estimation of complexity of the task, can be "Easy", "Medium" or "Hard"

# Risk of exceeding estimated time: String, Estimation of risk, can be "Not risky", "OK", "Risky", "Very risky" Calculated info:

# Correctness: Percentage %, Ratio of real time over the estimated time

# Estimated time by calc: HH:MM:SS, Estimated time for subsequent tasks using Correctness and Self estimated time to predict the estimated time

from django.db import models

LEVEL_CHOICES = [("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")]

RISK_CHOICES = [
    ("Not risky", "Not risky"),
    ("OK", "OK"),
    ("Risky", "Risky"),
    ("Very risky", "Very risky"),
]


class Task(models.Model):
    name = models.CharField(max_length=100)
    planning_time = models.TimeField()
    self_estimated_time = models.TimeField()
    real_time_spent = models.TimeField(null=True, blank=True)
    complexity_level = models.CharField(
        max_length=6, choices=LEVEL_CHOICES, null=True, blank=True
    )
    risk_of_exceeding_time = models.CharField(
        max_length=10, choices=RISK_CHOICES, null=True, blank=True
    )
    correctness = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    estimated_time_by_calc = models.TimeField(null=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Obligatory inputs: Name of the task, Planning Time, Self Estimated Time, Real time spent
# Optional inputs: Notes, Level, Risk
# Calculated inputs: Estimated time by calc, Correctness
