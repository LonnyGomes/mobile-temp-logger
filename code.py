import mount_sd
import epd
import dht
import bme

import time
import board
import digitalio
import busio
import adafruit_ds1307
import microcontroller

# pins definitions
PINS_I2C_DATA = board.GP2
PINS_I2C_CLOCK = board.GP3

# time in seconds to log data
LOG_INTERVAL = 60 * 6

# track max/min temps
maxTemp = None
minTemp = None

# set up i2c bus
i2c = busio.I2C(scl=PINS_I2C_CLOCK, sda=PINS_I2C_DATA)
rtc = adafruit_ds1307.DS1307(i2c)


def getLastUpdatedStr(t):
    return "%d%02d%02d %02d:%02d" % (
        t.tm_year,
        t.tm_mon,
        t.tm_mday,
        t.tm_hour,
        t.tm_min,
    )


def readOnboardTemp():
    temp_c = microcontroller.cpu.temperature
    temp_f = temp_c * (9 / 5) + 32

    return temp_f


days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if False:  # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2021, 8, 23, 18, 29, 00, 1, -1, -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

    print("Setting time to:", t)  # uncomment for debugging
    rtc.datetime = t

t = rtc.datetime
startDateStr = "%s %02d-%02d-%d" % (
    days[t.tm_wday],
    t.tm_mon,
    t.tm_mday,
    t.tm_year,
)

startTimeStr = "%d:%02d:%02d" % (
    t.tm_hour,
    t.tm_min,
    t.tm_sec,
)

csvFilename = "%d%02d%02d%02d%02d%02d.csv" % (
    t.tm_year,
    t.tm_mon,
    t.tm_mday,
    t.tm_hour,
    t.tm_min,
    t.tm_sec,
)
print(t)

print("Starting %s @ %s" % (startDateStr, startTimeStr))
mount_sd.createLogFile(csvFilename)

# epd.updateDisplay(startDateStr, startTimeStr, getLastUpdatedStr(t), 77, 66, 88)

while True:
    t = rtc.datetime
    # print(t)     # uncomment for debugging
    # print("The date is %s %d/%d/%d" % (days[t.tm_wday], t.tm_mday, t.tm_mon, t.tm_year))
    # print("The time is %d:%02d:%02d" % (t.tm_hour, t.tm_min, t.tm_sec))

    curTimestamp = "%d-%02d-%02dT%02d:%02d:%02d" % (
        t.tm_year,
        t.tm_mon,
        t.tm_mday,
        t.tm_hour,
        t.tm_min,
        t.tm_sec,
    )

    # read from external temperature sensor
    temp_ext, humid_ext = dht.readSensor()

    # read from bme sensor
    temp_alt, humid_alt = bme.readSensor()

    # read from onput pico sensor
    temp_f = readOnboardTemp()

    # determine the max/min temps based on all sensors
    if maxTemp is None:
        maxTemp = temp_f

    if minTemp is None:
        minTemp = temp_f

    if temp_ext is None:
        maxTemp = max(maxTemp, temp_f)
        minTemp = min(minTemp, temp_f)
    else:
        maxTemp = max(maxTemp, temp_f, temp_ext)
        minTemp = min(minTemp, temp_f, temp_ext)

    print(
        "Timestamp: %s, internal: %d, ext temp: %d, max: %d, min: %d, hum: %d"
        % (curTimestamp, temp_f, temp_ext, maxTemp, minTemp, humid_ext)
    )

    mount_sd.logData(
        csvFilename, curTimestamp, temp_f, temp_ext, humid_ext, temp_alt, humid_alt
    )

    epd.updateDisplay(
        startDateStr, startTimeStr, getLastUpdatedStr(t), temp_alt, minTemp, maxTemp
    )

    time.sleep(LOG_INTERVAL)
