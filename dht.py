import board
import adafruit_dht
import time

PIN_DHT = board.GP20

dht = adafruit_dht.DHT22(PIN_DHT)


def readSensor():
    temperature, humidity = sample_DHT(5, 6)

    return temperature, humidity


def sample_DHT(sleep_timer, retries):
    valid = 0
    invalid = 0
    temperature = 0
    humidity = 0
    while valid < 1:
        try:
            temperature = dht.temperature * (9 / 5) + 32
            humidity = dht.humidity
            valid += 1

        except RuntimeError as e:
            invalid += 1
            print("Reading from DHT failure: ", e.args)
            if invalid > retries:
                print("Retries exceeded Aborting")
                return 0, 0
            else:
                time.sleep(sleep_timer)

    return temperature, humidity
