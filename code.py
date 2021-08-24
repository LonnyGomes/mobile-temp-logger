import mount_sd
import time
import board
import digitalio
import busio
import adafruit_ds1307
import microcontroller

# pins definitions
PINS_I2C_DATA = board.GP2
PINS_I2C_CLOCK = board.GP3

# track max/min temps
maxTemp = None
minTemp = None

# set up i2c bus
i2c = busio.I2C(scl=PINS_I2C_CLOCK, sda=PINS_I2C_DATA)
rtc = adafruit_ds1307.DS1307(i2c)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if False:  # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2021, 8, 23, 18, 29, 00, 1, -1, -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

    print("Setting time to:", t)  # uncomment for debugging
    rtc.datetime = t

t = rtc.datetime
startTime = "%s %02d-%02d-%d @ %d:%02d:%02d" % (
    days[t.tm_wday],
    t.tm_mon,
    t.tm_mday,
    t.tm_year,
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

print("Starting %s" % (startTime))
mount_sd.createLogFile(csvFilename)

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
    temp_c = microcontroller.cpu.temperature
    temp_f = temp_c * (9 / 5) + 32
    if maxTemp is None or temp_f > maxTemp:
        maxTemp = temp_f

    if minTemp is None or temp_f < minTemp:
        minTemp = temp_f

    print(
        "Timestamp: %s, Temp cur: %d, max: %d, min: %d"
        % (curTimestamp, temp_f, maxTemp, minTemp)
    )

    mount_sd.logData(csvFilename, curTimestamp, temp_f)

    time.sleep(5)  # wait a second
