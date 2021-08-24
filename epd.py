import board
import busio
import displayio
import time
import terminalio
import adafruit_il0373
from adafruit_display_text import label


PIN_SCK = board.GP14
PIN_STX = board.GP15
PIN_SRX = board.GP12

PIN_ECS = board.GP28
PIN_DC = board.GP27
PIN_SRCS = board.GP26
PIN_RST = board.GP22
PIN_BUSY = board.GP21

displayio.release_displays()

spi = busio.SPI(clock=PIN_SCK, MOSI=PIN_STX, MISO=PIN_SRX)

display_bus = displayio.FourWire(
    spi, command=PIN_DC, chip_select=PIN_ECS, reset=PIN_RST, baudrate=1000000
)
time.sleep(1)

epd = adafruit_il0373.IL0373(
    display_bus,
    width=152,
    height=152,
    busy_pin=PIN_BUSY,
    highlight_color=0xFF0000,
    rotation=180,
)

time.sleep(epd.time_to_refresh)

print("Refreshed display")

def updateDisplay(startDateStr, startTimeStr, lastUpdatedStr, curTemp, minTemp, maxTemp):
    g = displayio.Group()
    text_started_hdr = label.Label(terminalio.FONT, text="Started ...", color = 0xFF0000)
    text_started_hdr.x = 10
    text_started_hdr.y = 10
    text_started_hdr.anchor_point = (0.5, 0.0)
    g.append(text_started_hdr)

    text_started = label.Label(terminalio.FONT, text=startDateStr, color = 0xFFFFFF)
    text_started.x = 10
    text_started.y = 25
    text_started.anchor_point = (0.5, 0.0)
    g.append(text_started)

    text_started_time = label.Label(terminalio.FONT, text="Time: %s" % (startTimeStr), color = 0xFF000)
    text_started_time.x = 10
    text_started_time.y = 40
    text_started_time.anchor_point = (0.5, 0.0)
    g.append(text_started_time)


    # cur temp
    text = label.Label(terminalio.FONT, text="Current: %d degs" % (curTemp), color = 0xFFFFFF)
    text.x = 10
    text.y = 60
    text.anchor_point = (0.5, 0.0)
    g.append(text)

    text = label.Label(terminalio.FONT, text="Min: %d degs" % (minTemp), color = 0xFFFFFF)
    text.x = 10
    text.y = 75
    text.anchor_point = (0.5, 0.0)
    g.append(text)

    text = label.Label(terminalio.FONT, text="Max: %d degs" % (maxTemp), color = 0xFFFFFF)
    text.x = 10
    text.y = 90
    text.anchor_point = (0.5, 0.0)
    g.append(text)

    text = label.Label(terminalio.FONT, text="Last updated:", color = 0xFF0000)
    text.x = 10
    text.y = 120
    text.anchor_point = (0.5, 0.0)
    g.append(text)

    text = label.Label(terminalio.FONT, text=lastUpdatedStr, color = 0xFFFFFF)
    text.x = 10
    text.y = 135
    text.anchor_point = (0.5, 0.0)
    g.append(text)

    epd.show(g)

    epd.refresh()

    # (optional) wait until display is fully updated
    while epd.busy:
        pass

    print("display updated!")
