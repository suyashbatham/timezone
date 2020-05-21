import pytz
import datetime
# country = 'Europe/Moscow'
# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("the time is{} in {}".format(country,local_time))
# print("UTC is {}".format(datetime.datetime.utcnow()))
#
# for x in pytz.all_timezones:
#     print(x)

# for x in sorted(pytz.country_names):
#     print(x+" ;"+pytz.country_names[x])
# for x in sorted(pytz.country_names):
#     print("{} : {}: {}".format(x,pytz.country_names[x],pytz.country_timezones.get(x)))

for x in sorted(pytz.country_names):
    print("{} : {}".format(x,pytz.country_names[x],end=';'))
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone,local_time))
        print(pytz.country_timezones[x])
    else:
        print("\t\tNo time zone exist in such area")