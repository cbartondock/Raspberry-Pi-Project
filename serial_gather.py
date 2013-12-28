import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()
while True:
    btr=ser.readline()
    parts=btr.split(',')
    if(parts[0]=="$GPRMC"):
        print(btr)
        for i in range(0,len(parts)):
            if parts[i] == 'N' or parts[i] =='S':
                latitude = float(parts[i-1])
            if parts[i] == 'W' or parts[i] == 'E':
                longitude = float(parts[i-1])
