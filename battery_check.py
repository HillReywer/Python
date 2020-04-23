# pip3 install psutil

import psutil

battery = psutil.sensors_battery()

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))