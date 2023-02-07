# TODO: reorder imports
#   Imports should be grouped in the following order:
#       Standard library imports.
#       Related third party imports.
#       Local application/library specific imports.
from .models import Task
from django.db.models import Avg
import datetime


# TODO: Add typing input/output + docstring
#   Two blank space at top level
def time_in_sec(time_obj):
    time_obj = str(time_obj)
    time_arr = datetime.datetime.strptime(time_obj, '%H:%M:%S')
    total_time_sec = datetime.timedelta(hours=time_arr.hour, minutes=time_arr.minute).seconds
    return total_time_sec


# TODO: Add typing input/output + docstring
#   Two blank space at top level
def get_correctness(real_time, estimated_time):
    return (time_in_sec(real_time) / time_in_sec(estimated_time)) * 100


# TODO: Add typing input/output + docstring
#   Two blank space at top level
def get_estimation_time(estimated_time):
    # TODO: Delete comments if unused
    # Estimated time by calc 
    # (average correctness / 100) * estimated time

    # TODO: For readability, you can put this on multiple line
    avg_correctness = Task.objects.exclude(
        correctness__isnull=True
    ).aggregate(
        avg_correctness=Avg('correctness')
    )

    if avg_correctness['avg_correctness'] is not None:
        estimated_by_calc_sec = round(avg_correctness['avg_correctness'])/100 * time_in_sec(estimated_time)
        estimated_by_calc = str(datetime.timedelta(seconds=estimated_by_calc_sec))
    else:
        estimated_by_calc = None
    return estimated_by_calc
