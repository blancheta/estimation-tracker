from django.db import models
from datetime import datetime


# Create your models here.

class Task(models.Model):
    LEVEL = (
        ('-', '-'),
        ('Easy', 'easy'),
        ('Medium', 'medium'),
        ('Hard', 'Hard')
    )
    RISK = (
        ('-', '-'),
        ('Not risky', 'not risky'),
        ('OK', 'OK'),
        ('Risky', 'risky'),
        ('Very risky', 'very risky')
    )

    name = models.CharField(max_length=100, null=True)
    planning = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    estimate = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    realtime = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    risk = models.CharField(max_length=100, null=True, choices=RISK)
    level = models.CharField(max_length=100, null=True, choices=LEVEL)
    notes = models.CharField(max_length=253, null=True)
    estimateb_by_calc = models.CharField(max_length=253, null=True)
    correctness = models.IntegerField(null=True)

    # realtime = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


"""
    def calc (self):
        time1 = datetime.strptime('12:45', '%H:%M').time()
        time2 = datetime.strptime(self.estimate, '%H:%M').time()
        #time_1 = time1.total_seconds()
        #time_2 = time2.total_seconds()
        #calcul = time_2+time_1
        return time1
"""
