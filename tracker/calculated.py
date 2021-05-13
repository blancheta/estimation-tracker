
from datetime import datetime, timedelta

def calc_estimation_time(estimate, realtime):
    # calculation of estimateb_by_calc from user data
    estimated_dt = datetime.strptime(estimate, '%H:%M')
    realtime_dt = datetime.strptime(realtime, '%H:%M')

    estimated_duration_td = timedelta(hours=estimated_dt.hour, minutes=estimated_dt.minute)
    realtime_duration_td = timedelta(hours=realtime_dt.hour, minutes=realtime_dt.minute)

    diff_td = realtime_duration_td - estimated_duration_td
    seconds = diff_td.seconds
    estimate_by_calc = f"{int(seconds / 3600)}"+f': {(int(seconds / 60)) % 60} '
    return estimate_by_calc


def calc_correctness(estimate, realtime):
    # calculation of correctness from user data
    estimated_dt = datetime.strptime(estimate, '%H:%M')
    realtime_dt = datetime.strptime(realtime, '%H:%M')

    estimated_duration_td = timedelta(hours=estimated_dt.hour, minutes=estimated_dt.minute)
    realtime_duration_td = timedelta(hours=realtime_dt.hour, minutes=realtime_dt.minute)

    correctness = 100 * realtime_duration_td.seconds / estimated_duration_td.seconds
    return correctness