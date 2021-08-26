import storage
import board
import busio
import sdcardio


PIN_SCK = board.GP6
PIN_STX = board.GP7
PIN_SRX = board.GP4
PIN_CS = board.GP5

spi = busio.SPI(clock=PIN_SCK, MOSI=PIN_STX, MISO=PIN_SRX)
cs = PIN_CS

sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")


def createLogFile(filename):
    fullPath = "/sd/%s" % (filename)
    with open(fullPath, "w") as f:
        print("Creating CSV: %s:" % (fullPath))

        # create CSV header
        f.write("timestamp,temp_int,temp_ext,humidty_ext,temp_alt,humidty_alt\n")


def logData(
    filename, timestamp, temp_int, temp_ext, humidty_ext, temp_alt, humidty_alt
):
    fullPath = "/sd/%s" % (filename)
    with open(fullPath, "a") as f:
        f.write(
            "%s,%s,%s,%s,%s,%s\n"
            % (timestamp, temp_int, temp_ext, humidty_ext, temp_ext, humidty_alt)
        )
