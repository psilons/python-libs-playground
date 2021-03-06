import ephem

import datetime
import pytz
from tzwhere import tzwhere
import numpy as np


def time_zone(latitude, longitude):
    tz_where = tzwhere.tzwhere()
    timezone_str = tz_where.tzNameAt(latitude, longitude)
    return pytz.timezone(timezone_str)


def utc_time(date_time: str, time_tz):  # convert date_time in time_tz timezone to utc time
    local_time = time_tz.localize(datetime.datetime.fromisoformat(date_time))  # "2012-12-12 10:10:10"
    return local_time.astimezone(pytz.utc)


def get_shadow_length(latitude, longitude, date_time, height=1):
    """
    Accepts longitude and latitude in the WGS84 CRS, along with the
    datetime in the UTC time zone. Returns the length of a shadow of an object
    with a specified height at the specified time and location.
    """
    obs_tz = time_zone(latitude, longitude)
    print(f'observer timezone: {obs_tz}')
    obs_utc_time = utc_time(date_time, obs_tz)
    print(f'observer utc time: {obs_utc_time}')

    o = ephem.Observer()
    o.long, o.lat = str(longitude), str(latitude)
    o.date = ephem.Date(obs_utc_time)

    sun = ephem.Sun(o)
    print(sun.alt)

    shadow = height / np.tan(sun.alt)
    return shadow


def test1():
    # beijing
    # print(get_shadow_length('39.9042', '116.4074', '2001/01/01 1:00'))
    print(get_shadow_length(39.9042, 116.4074, '1984-06-30 09:15:56'))
    print(time_zone(42.37, -71.03))  # America/New_York
    print(time_zone(39.9042, 116.4074))  # Asia/Shanghai


##############################################################################################
def daily_min_shadow(obs_tz, obs, dt, height=1):
    dt_begin = datetime.datetime(dt.year, dt.month, dt.day)
    utc_begin = obs_tz.localize(dt_begin).astimezone(pytz.utc)

    dt_end = datetime.datetime(dt.year, dt.month, dt.day, 23, 59, 59)
    utc_end = obs_tz.localize(dt_end).astimezone(pytz.utc)

    time = utc_begin
    obs.date = ephem.Date(time)

    intv = datetime.timedelta(minutes=5)
    sun = ephem.Sun(obs)
    shadow = 1000
    while time < utc_end:
        # print(f'observer utc time: {time}')
        sun.compute(obs)
        # print(f'Sun altitude: {sun.alt}')
        cs = height / np.tan(sun.alt)
        if cs > 0:
            shadow = min(shadow, height / np.tan(sun.alt))

        time += intv
        obs.date = ephem.Date(time)

    return shadow


def test2():
    latitude, longitude = 39.91369, 116.38824

    obs_tz = time_zone(latitude, longitude)
    print(f'observer timezone: {obs_tz}')

    observer = ephem.Observer()
    observer.lat, observer.long = str(latitude), str(longitude)

    dt = datetime.datetime.fromisoformat('2021-12-11')

    print(daily_min_shadow(obs_tz, observer, dt))


# test2()  # 1.9538522969767638

######################################################################################
def yearly_mins(latitude, longitude, year):
    obs_tz = time_zone(latitude, longitude)
    print(f'observer timezone: {obs_tz}')

    observer = ephem.Observer()
    observer.lat, observer.long = str(latitude), str(longitude)

    year_begin = datetime.datetime(year, 1, 1)
    year_end = datetime.datetime(year, 12, 31)
    days = (year_end - year_begin).days + 1
    res = []
    for i in range(days):
        dt = year_begin + datetime.timedelta(i)
        res.append(daily_min_shadow(obs_tz, observer, dt))

    return res


print(yearly_mins(39.91369, 116.38824, 2021))
