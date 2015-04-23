import MySQLdb
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
pin=11

db = MySQLdb.connect("sql5.freesqldatabase.com","sql574954","cM7*lB7!","sql574954")

cursor = db.cursor()
clear = "TRUNCATE TABLE SENSORS"
insertvals = "INSERT INTO SENSORS(GPSLAT,GPSLONG,ULTRA,TIME) VALUES ('{lat}','{lon}','{ultra}','{time}')"
cursor.execute(clear)
for i in range(0,100):
    measurement = measure()
    time.sleep(.000007)
    currenttime=time.strftime('%Y-%m-%d %H:%M:%S')
    print("({0},{1})".format(currenttime,measurement))
    try:
        cursor.execute(insertvals.format(lat=0,lon=0,ultra=measurement,time=currenttime))
        db.commit()
    except:
        print("insert failed")
        db.rollback()
db.close()






def measure():
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
    return 17015*duration
