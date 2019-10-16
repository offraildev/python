import datetime
import pytz

d = datetime.date(2019, 6, 22)
tday = datetime.date.today()

tdelta = datetime.timedelta(days=7)

bday = datetime.date(2020, 4, 30)


print(f'Days till birthday {(bday-tday).total_seconds()}')
print(tday.isoweekday())
print(tday.weekday())


time = datetime.time(6, 5, 50, 56566) 
print(time)

dt = datetime.datetime(2020, 4, 30, 6, 5, 50, 56566)

print(dt.time())
print(dt.date())

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

#  aware datetimes 

dt = datetime.datetime(2020, 4, 30, 6, 5, 50, 56566, tzinfo=pytz.UTC)
print(dt)

dt_utc_now = datetime.datetime.now(tz=pytz.UTC)
print(dtnow)

dt_mtn = dt_utc_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

# all timezones
for tz in pytz.all_timezones:
    print(tz)

# localize naive timezone to aware timezone
dt_now = datetime.datetime.now()
mnt_tz = pytz.timezone('US/Mountain')

dt_utc_now = mnt_tz.localize(dt_now)
dt_utc_east = dt_utc_now.astimezone(pytz.timezone('US/Eastern'))

print(dt_utc_east)

# international time format

dt = datetime.datetime.today()
print(dt)

# date to string
str_fmt = dt.strftime('%B %d, %y')
print(str_fmt)

# string to date
print(datetime.datetime.strptime('June 22, 19', '%B %d, %y'))





