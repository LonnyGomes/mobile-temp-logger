
import time
import board
import digitalio
import busio
import adafruit_ds1307

# pins definitions
PINS_I2C_DATA = board.GP2
PINS_I2C_CLOCK = board.GP3


# define flags to keep state
isTargetDay = False
servoNeedsChange = True

# set up i2c bus
i2c = busio.I2C(scl=PINS_I2C_CLOCK, sda=PINS_I2C_DATA)
rtc = adafruit_ds1307.DS1307(i2c)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if False:   # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2021,  8,   23,   18,  29,  00,    1,   -1,    -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

    print("Setting time to:", t)     # uncomment for debugging
    rtc.datetime = t
    print()

while True:
    t = rtc.datetime
    #print(t)     # uncomment for debugging
    print("The date is %s %d/%d/%d" % (days[t.tm_wday], t.tm_mday, t.tm_mon, t.tm_year))
    print("The time is %d:%02d:%02d" % (t.tm_hour, t.tm_min, t.tm_sec))

    time.sleep(5) # wait a second
