import datetime
import time
import pytz

available_zones = {'1':'Africa/Tunis',
                   '2':'Asia/Kolkata',
                   '3':'Austraila/Adelaide',
                   '4':'Europse/Brussels',
                   '5':'Europe/London',
                   '6':'Japan',
                   '7':'Pacific/Tahiti',
                   '8':'US/Hawaii',
                   '9':'Zulu'}
print("Please choose a time zone (or 0 to quit:)")
for plcae in sorted(available_zones):
    print("\t{}.{}".format(plcae,available_zones[plcae]))

while True:
    choose = input()
    if choose=='0':
        break
    if choose in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choose])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in{} is{} {} ".format(available_zones[choose],world_time.strftime('%A' '%x' '%X' '%z'),world_time.tzname()))
        print("Local time is{}".format(datetime.datetime.now().strftime('%A' '%x' '%X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A' '%x' '%X')))