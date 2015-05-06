import wiringpi2 as wp
import sys
wp.wiringPiSetupGpio()
for i in range(0,30):
    try:
	wp.pinMode(i,1)
	wp.digitalWrite(i,0)
	wp.pinMode(i,0)
    except:
	print("Cleanup on GPIO pin "+str(i)+" failed")
	print("Error was: ",sys.exc_info()[0])
	raise
