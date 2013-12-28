import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

try:
    while True:
        GPIO.output(7,True)
finally:
    GPIO.output(7,False)
