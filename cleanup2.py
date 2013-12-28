import wiringpi2 as wp
import time
import sys
wp.wiringPiSetupPhys()
for i in [3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26]:
    print i
    try:
	    wp.pinMode(i,1)
	    wp.digitalWrite(i,0)
	    wp.pinMode(i,0)
    except:
	    print("Cleanup on GPIO pin "+str(i)+" failed")
	    print("Error was: ",sys.exc_info()[0])
	    raise
