from django import forms

from .models import Task
from .utils import get_correctness, get_estimation_time


class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "planning_time",
            "self_estimated_time",
            "real_time_spent",
            "complexity_level",
            "risk_of_exceeding_time",
            "notes",
        ]

        widgets = {
            "planning_time": forms.TimeInput(
                format="%H:%M:%S", attrs={"type": "time", "step": "1"}
            ),
            "self_estimated_time": forms.TimeInput(
                format="%H:%M:%S", attrs={"type": "time", "step": "1"}
            ),
            "real_time_spent": forms.TimeInput(
                format="%H:%M:%S", attrs={"type": "time", "step": "1"}
            ),
        }

    def save(self, *args, commit=True):
        task = super(CreateTask, self).save(*args, commit=False)
        if self.is_valid() and self.cleaned_data["real_time_spent"]:
            # calculate estimated_time_by_calc & correctness before savibng
            task.estimated_time_by_calc = get_estimation_time(
                self.cleaned_data["self_estimated_time"]
            )
            task.correctness = get_correctness(
                self.cleaned_data["real_time_spent"],
                self.cleaned_data["self_estimated_time"],
            )
            if commit:
                task.save()
        return task
