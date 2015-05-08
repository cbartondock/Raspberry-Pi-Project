import MySQLdb
import wiringpi2 as wp
import time
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()

wp.wiringPiSetupPhys()

def measure_gps():
    check=True
    latitude=-1
    longitude=-1
    while check:
        btr=ser.readline()
        parts=btr.split(',')
        if parts[0]=="$GPRMC":
            check=False
            for i in range(0,len(parts)):
                if parts[i] == 'N' or parts[i] =='S':
                    latitude = float(parts[i-1])
                if parts[i] == 'W' or parts[i] == 'E':
                    longitude = float(parts[i-1])
    return [latitude, longitude]

def measure_ultra(pin):
    wp.pinMode(pin,1)

    #zero output
    wp.digitalWrite(pin,0)
    time.sleep(.000002)

    #send signal
    wp.digitalWrite(pin,1)
    time.sleep(.000005)
    wp.digitalWrite(pin,0)

    #receive signal
    wp.pinMode(pin,0)
    while wp.digitalRead(pin)==0:
        starttime=time.time()
    while wp.digitalRead(pin)==1:
        endtime=time.time()
    duration= endtime-starttime
    return 17015*duration

db = MySQLdb.connect("sql4.freesqldatabase.com","sql476380","eW4%sG5%","sql476380")

cursor = db.cursor()
#clear = "TRUNCATE TABLE SENSORS"
clear="""
TRUNCATE TABLE SENSORS
"""

insertvals = "INSERT INTO SENSORS(GPSLAT,GPSLONG,ULTRAF,ULTRAB,ULTRAL,ULTRAR,TIME) VALUES ('{lat}','{lon}','{ultraf}','{ultrab}','{ultral}','{ultrar}','{time}')"
print("clearing table")
#cursor.execute(clear)
print("done clearing")
ultrapins=[12,11,8,7]
try:
    while True:
        ums = [measure_ultra(upin) for upin in ultrapins]
        gps = measure_gps()
        time.sleep(.000007)
        currenttime=time.strftime('%Y-%m-%d %H:%M:%S')
        print("({0},{1},{2})".format(currenttime,ums,gps))
        
        try:
            cursor.execute(insertvals.format(lat=gps[0],lon=gps[1],ultraf=ums[0],ultrab=ums[1],ultral=ums[2],ultrar=ums[3],time=currenttime))
            db.commit()
        except:
            print("insert failed")
            db.rollback()
finally:
    db.close()







