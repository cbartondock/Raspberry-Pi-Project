import MySQLdb
import wiringpi2 as wp
import time
wp.wiringPiSetupPhys()
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
clear = "TRUNCATE TABLE SENSORS"
insertvals = "INSERT INTO SENSORS(GPSLAT,GPSLONG,ULTRAF,ULTRAB,ULTRAL,ULTRAR,TIME) VALUES ('{lat}','{lon}','{ultraf}','ultrab','ultral','ultrar','{time}')"
cursor.execute(clear)
#for i in range(0,100):
while True:
    measurement = measure_ultra(32)
    time.sleep(.000007)
    currenttime=time.strftime('%Y-%m-%d %H:%M:%S')
    print("({0},{1})".format(currenttime,measurement))
    try:
        cursor.execute(insertvals.format(lat=0,lon=0,ultraf=measurement,ultrab=0.1,ultral=0.1,ultrar=0.1,time=currenttime))
        db.commit()
    except:
        print("insert failed")
        db.rollback()
db.close()







