import RPi.GPIO as GPIO
import time
from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

import I2C_driver as LCD
from time import *


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def main():
    LED = 12
    Flame = 15
    Light = 13
    Switch = 10
    Flag1 = Flag2 = Flag3 = 0
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Flame, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Light, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

    mylcd = LCD.lcd()

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)

    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while True:
        if (GPIO.input(Switch) == GPIO.HIGH and Flag1 == 0):
            print("Touch ON")
            Flag1 = 1
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'T', fill="white", font=proportional(CP437_FONT))
                sleep(2)

        elif (GPIO.input(Switch) == GPIO.LOW and Flag1 == 1):
            print("Touch OFF")
            Flag1 = 0
            with canvas(virtual) as draw:
                text(draw, (0, 1), ' ', fill="white", font=proportional(CP437_FONT))
                sleep(2)

        elif (GPIO.input(Flame) == GPIO.HIGH and Flag2 == 0):
            print("Flame ON")
            Flag2  = 1
            for i in range(20):
                GPIO.output(LED, GPIO.HIGH)
                sleep(0.5)
                GPIO.output(LED, GPIO.LOW)
                sleep(0.5)
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'F', fill="white", font=proportional(CP437_FONT))
                sleep(2)

        elif (GPIO.input(Flame) == GPIO.LOW and Flag2 == 1):
            print("Flame OFF")
            Flag2  = 0
            with canvas(virtual) as draw:
                text(draw, (0, 1), ' ', fill="white", font=proportional(CP437_FONT))
                sleep(2)

        elif (GPIO.input(Light) == GPIO.HIGH and Flag3 == 1):
            print("Light ON")
            Flag3 = 0
            mylcd.lcd_display_string("Room Light ON",1)
            sleep(5)
            mylcd.lcd_clear()
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'L', fill="white", font=proportional(CP437_FONT))
                sleep(2)

        elif (GPIO.input(Light) == GPIO.LOW and Flag3 == 0):
            print("Light OFF")
            Flag3 = 1
            with canvas(virtual) as draw:
                text(draw, (0, 1), ' ', fill="white", font=proportional(CP437_FONT))
                sleep(2)
'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
