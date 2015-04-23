import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
pin=11
GPIO.setup(pin,GPIO.OUT)

#zero output
GPIO.output(pin,0)
time.sleep(.000002)

#send signal
GPIO.output(pin,1)
time.sleep(.000005)
GPIO.output(pin,0)

#receive signal
GPIO.setup(pin,GPIO.IN)
while GPIO.input(pin)==0:
	starttime=time.time()
while GPIO.input(pin)==1:
	endtime=time.time()
duration= endtime-starttime	
print(str(17015*duration))
