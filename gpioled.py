import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

LED_RED = 3
LED_GREEN = 5
LED_BLUE = 7

GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

while 1:

	#RED
	GPIO.output(5, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(5, GPIO.LOW)
	time.sleep(1)

	#BLUE
	GPIO.output(7, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(7, GPIO.LOW)
	time.sleep(1)

	#RED
	GPIO.output(3, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(3, GPIO.LOW)
	time.sleep(1)
