import time
import wiringpi2 as wp
wp.wiringPiSetupPhys()
wp.pinMode(29,1)
while True:
    print("hi")
    
    time.sleep(2)
    wp.digitalWrite(29,0)
    
    time.sleep(2)
    wp.digitalWrite(29,1) 
