import datetime
from typing import Union

from django.db.models import Avg

from .models import Task


def time_in_sec(time_obj: datetime.time) -> int:
    """
    It takes a time object and returns the total time in seconds.

    :return: The total time in seconds.
    """
    time_obj = str(time_obj)
    time_arr = datetime.datetime.strptime(time_obj, "%H:%M:%S")
    total_time_sec = datetime.timedelta(
        hours=time_arr.hour, minutes=time_arr.minute
    ).seconds
    return total_time_sec


def get_correctness(real_time: datetime.time, estimated_time: datetime.time) -> float:
    """
    It takes two time objects and returns what percentage is the real time compared to the estimated time.

    :return: A float ratio of the real time compared to the estimated time.
    """
    return (time_in_sec(real_time) / time_in_sec(estimated_time)) * 100


def get_estimation_time(estimated_time: datetime.time) -> Union[str, None]:
    """
    It takes a time object and returns a string of the estimated time based on the average correctness
    of all tasks

    :return: A string of the estimated time
    """

    avg_correctness = Task.objects.exclude(correctness__isnull=True).aggregate(
        avg_correctness=Avg("correctness")
    )
    if avg_correctness["avg_correctness"] is not None:
        # Estimated time by calc = (average correctness / 100) * estimated time
        estimated_by_calc_sec = (
            round(avg_correctness["avg_correctness"])
            / 100
            * time_in_sec(estimated_time)
        )
        estimated_by_calc = str(datetime.timedelta(seconds=estimated_by_calc_sec))
    else:
        estimated_by_calc = None
    return estimated_by_calc
