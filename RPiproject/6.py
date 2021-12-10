import RPi.GPIO as GPIO
import I2C_driver
import time
import random
from time import sleep, strftime
from datetime import datetime
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

mylcd = I2C_driver.lcd()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 12

def main():

    #mylcd = rasp1012.lcd()
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)
    
    n = str(input())
    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while 1:
        if (n == 'LED'):
            GPIO.output(12, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(12, GPIO.LOW)
            time.sleep(1)
                
        elif (n == 'LCD'):
            mylcd.lcd_display_string("Raspberry PI",1)
            mylcd.lcd_display_string("LCD Display test",2)
            time.sleep(3)
            mylcd.lcd_clear()

        elif (n == 'DOT'):
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'O', fill="white", font=proportional(CP437_FONT))
            time.sleep(2)
            with canvas(virtual) as draw:
                text(draw, (0, 1), '', fill="white", font=proportional(CP437_FONT))
            time.sleep(2)
            
        n = str(input())

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''
if __name__ == '__main__':
    main()


