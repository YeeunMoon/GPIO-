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
Touch = 10
Flame = 8
Light = 13
Button = 7

def main():

    #mylcd = rasp1012.lcd()
    GPIO.setup(Touch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Flame, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Light, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED, GPIO.OUT)

    PWM_LED = GPIO.PWM(LED, 50)
    PWM_LED.start(0)

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)

    n = 0
    listsum = 0
    list = []
    
    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while True:
        if (GPIO.input(Button) == GPIO.HIGH):
            n = random.randint(1, 3)
            list.append(n)
            listsum = sum(list)
            print("Button On", n)
            time.sleep(0.5)
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(listsum) , fill="white", font=proportional(CP437_FONT))
                
            if listsum >= 10:
                mylcd.lcd_display_string("Button ON",1)
                time.sleep(2)
                mylcd.lcd_clear()

        if (GPIO.input(Touch) == GPIO.HIGH):
            n = random.randint(1, 3)
            list.append(n)
            listsum = sum(list)
            print("Touch ON", n)
            time.sleep(0.5)
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(listsum) , fill="white", font=proportional(CP437_FONT))
            if listsum >= 10:
                mylcd.lcd_display_string("Touch ON",1)
                time.sleep(2)
                mylcd.lcd_clear()

        if (GPIO.input(Light) == GPIO.HIGH):
            n = random.randint(1, 3)
            list.append(n)
            listsum = sum(list)
            print("Light On", n)
            time.sleep(2)
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(listsum) , fill="white", font=proportional(CP437_FONT))
            if listsum >= 10:
                mylcd.lcd_display_string("Light ON",1)
                time.sleep(2)
        
        if (GPIO.input(Flame) == GPIO.HIGH):
            n = random.randint(1, 3)
            list.append(n)
            listsum = sum(list)
            print("Flame ON", n)
            sleep(1)
            with canvas(virtual) as draw:
                text(draw, (0, 1), str(listsum) , fill="white", font=proportional(CP437_FONT))
            if listsum >= 10:
                mylcd.lcd_display_string("Flame ON",1)
                time.sleep(2)

        if listsum >= 10:
            for duty in range(100, -1, -5):
                PWM_LED.ChangeDutyCycle(duty)
                time.sleep(0.05)
                
                #time.sleep(0.5)
'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''
if __name__ == '__main__':
    main()

