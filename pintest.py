import time
import wiringpi2 as wp
wp.wiringPiSetupPhys()
tpin=7
wp.pinMode(tpin,1)
while True:
    time.sleep(1)
    wp.digitalWrite(tpin,0)
    wp.pinMode(tpin,0)
    print("read off: ",wp.digitalRead(tpin))
    wp.pinMode(tpin,1)
    time.sleep(1)
    wp.digitalWrite(tpin,1)
    wp.pinMode(tpin,0)
    print("read on: ",wp.digitalRead(tpin))
    wp.pinMode(tpin,1)

