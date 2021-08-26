# Mobile Temperature Logger

Logs periodic temperature readings for later analysis.

The main intent for this project is to measure how hot my car can get throughout the day.

![photo of prototype](images/prototype.jpg)

## Parts

- [Raspberry Pico](https://www.microcenter.com/product/632771/raspberry-pi-pi-pico-microcontroller-development-board-based-on-the-raspberry-pi-dual-core-arm-cortex-m0-rp2040-processor,-up-to-133-mhz,-supports-c-c)
- [Adafruit 152x152 Tri-Color eInk / ePaper Display](https://www.adafruit.com/product/3625)
- [Adafruit BME280 Temperature Humidity Pressure Sensor](https://www.adafruit.com/product/2652)
- [AM2302 temperature / humidity sensor](https://www.adafruit.com/product/393)
- [OSEP Real-time Clock & microSD Breakout](https://www.osepp.com/electronic-modules/breakout-boards/95-real-time-clock-microsd-breakout)
- [Vilros 3 AA Battery Holder With Micro USB Connector](https://www.microcenter.com/product/636558/vilros-3-aa-battery-holder-with-micro-usb-connector-for-raspberry-pi-pico)
- [32 GB Micro SD card](https://www.microcenter.com/product/485584/micro-center-32gb-microsdhc-card-class-10-flash-memory-card-with-adapter)
- [CR1220 Lithium Ion Cell](https://www.adafruit.com/product/380)
- [3 AA Lithium Ion Batterries](https://www.microcenter.com/product/605673/energizer-ultimate-lithium-aa-lithium-battery-4-pack)

## Circuit Python dependencies

- adafruit_bme280
- adafruit_dht.mpy
- adafruit_ds1307.mpy
- adafruit_register
- adafruit_bus_device
- adafruit_display_text
- adafruit_il0373.mpy
