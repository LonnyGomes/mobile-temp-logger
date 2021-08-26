import time
import board
import digitalio
import busio
from adafruit_bme280 import basic as adafruit_bme280

# pins definitions
PINS_I2C_DATA = board.GP8
PINS_I2C_CLOCK = board.GP9

# set up i2c bus
i2c = busio.I2C(scl=PINS_I2C_CLOCK, sda=PINS_I2C_DATA)

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)


def readSensor():
    temperature = bme280.temperature * (9 / 5) + 32
    humidity = bme280.relative_humidity

    print("\nBME Temperature: %0.1f F" % temperature)
    print("BME Humidity: %0.1f %%" % humidity)

    return temperature, humidity
