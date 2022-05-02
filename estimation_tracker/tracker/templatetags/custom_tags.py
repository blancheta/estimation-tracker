from django import template
import datetime
import math

register = template.Library()


def convert_time_to_seconds(time: datetime.time) -> int:
    seconds = (time.hour * 60 + time.minute) * 60 + time.second

    return seconds


def calculate_correctness_ratio(
    task_real_time: datetime.time, task_self_estimated_time: datetime.time
) -> int:
    
    real_time_seconds = convert_time_to_seconds(task_real_time)
    estimated_time_seconds = convert_time_to_seconds(task_self_estimated_time)

    return round((real_time_seconds / estimated_time_seconds) * 100)


def estimate_time(
    task_real_time: datetime.time, task_self_estimated_time: datetime.time
) -> datetime.time:
    
    correctness_ratio = calculate_correctness_ratio(
        task_real_time, task_self_estimated_time
    )
    correctness_ratio_rounded = math.ceil(correctness_ratio / 100) * 100

    estimate_time_multiplication_base = correctness_ratio_rounded / 100
    estimated_time_seconds = (
        convert_time_to_seconds(task_self_estimated_time)
        * estimate_time_multiplication_base
    )

    return datetime.timedelta(seconds=estimated_time_seconds)


register.simple_tag(calculate_correctness_ratio)
register.simple_tag(estimate_time)
