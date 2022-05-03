from django import template
import datetime
import math

register = template.Library()


def convert_time_to_seconds(time: datetime.time) -> float:
    """Convert datetime.time object to seconds.

    Args:
        time (datetime.time): Object containing time info.

    Returns:
        float: Total number of seconds.
    """
    
    seconds = datetime.timedelta(
        hours=time.hour, minutes=time.minute, seconds=time.second
    ).total_seconds()
    
    return seconds


def calculate_correctness_ratio(
    task_real_time: datetime.time, task_self_estimated_time: datetime.time
) -> int:
    """Percentage %, Ratio of real time over the estimated time

    Args:
        task_real_time (datetime.time): Time when task was finished.
        task_self_estimated_time (datetime.time): Estimated task finish time.

    Returns:
        int: Calculated task estimation accuracy (percentage).
    """

    real_time_seconds = convert_time_to_seconds(task_real_time)
    estimated_time_seconds = convert_time_to_seconds(task_self_estimated_time)

    return round((real_time_seconds / estimated_time_seconds) * 100)


def estimate_time(
    task_real_time: datetime.time, task_self_estimated_time: datetime.time
) -> datetime.time:
    """Estimated time for subsequent tasks using Correctness
    and Self estimated time to predict the estimated time.

    Args:
        task_real_time (datetime.time): Time when task was finished.
        task_self_estimated_time (datetime.time): Estimated task finish time.

    Returns:
        datetime.time: Auto calculated estimation time.
    """

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
