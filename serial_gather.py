import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()
while True:
	btr=ser.readline()
	print(btr)
