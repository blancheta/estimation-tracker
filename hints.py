from datetime import datetime, timedelta

estimated_duration = "02:00"
realtime_duration = "04:00"

estimated_dt = datetime.strptime(estimated_duration, '%H:%M')

realtime_dt = datetime.strptime(realtime_duration, '%H:%M')

estimated_duration_td = timedelta(hours=estimated_dt.hour, minutes=estimated_dt.minute)
realtime_duration_td = timedelta(hours=realtime_dt.hour, minutes=realtime_dt.minute)

diff_td = realtime_duration_td - estimated_duration_td
seconds = diff_td.seconds
print(f'Hours:{int(seconds / 3600)}')
print(f'Minutes:{(int(seconds / 60)) % 60}')

print('Correctness:', 100 * realtime_duration_td.seconds / estimated_duration_td.seconds, '%')
