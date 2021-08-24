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
        # create CSV header
        f.write("timestamp,temperature\n")


def logData(filename, timestamp, temperature):
    fullPath = "/sd/%s" % (filename)
    with open(fullPath, "a") as f:
        f.write("%s,%s\n" % (timestamp, temperature))
