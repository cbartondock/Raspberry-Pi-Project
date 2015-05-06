import time
import wiringpi2 as wp
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


rpins =[29,31,33,35,37]
tpins=[12,11,13,15,16]
ultrapins=[32,36,38,40]
ron =[0,0,0,0,0]
ton =[0,0,0,0,0]

for rpin in rpins:
    print(rpin)
    wp.pinMode(rpin,1)
    wp.digitalWrite(rpin,0)
print("\n\n")
for tpin in tpins:
    print(tpin)
    wp.pinMode(tpin,1)
    wp.digitalWrite(tpin,0)
for upin in ultrapins:
    print(ultrapin)
    wp.pinMode(upin,0)
print("\n")
thrust=0
thrustmax=31
rot=0
rotmax=31


bitarray32 = lambda n: map(int,list("0"*(5-len(bin(n)[2:]))+bin(n)[2:]))

db = MySQLdb.connect("sql4.freesqldatabase.com","sql574954","cM7*lB7!","sql574954")

cursor = db.cursor()
clear = "TRUNCATE TABLE SENSORS"
insertvals = "INSERT INTO SENSORS(GPSLAT,GPSLONG,ULTRAF,ULTRAB,ULTRAL,ULTRAR,TIME) VALUES ('{lat}','{lon}','{ultraf}','ultrab','ultral','ultrar','{time}')"
cursor.execute(clear)

try:
    while True:
        key = raw_input("-->")
    print("keypress")
    if key =="f":
        umeasure = [measure_ultra(i) for i in ultrapins]
        print("ultras measured: ",str(ultras))
        time.sleep(.000007)
        currenttime=time.strftime('%Y-%m-%d %H:%M:%S')
        try:
            cursor.execute(insertvals.format(lat=0,lon=0,ultraf=umeasure[0],ultrab=umeasure[1],ultral=umeasure[2],ultrar=umeasure[3],time=currenttime))
            db.commit()
        except:
            print("insert failed")
            db.rollback()
    if key =="w":
        if thrust <thrustmax:
            thrust+=1
    if key== "s":
        if thrust>0:
            thrust-=1
    if key =="d":
        if rot < rotmax:
            rot+=1
    if key=="a":
        if rot>0:
            rot-=1
    ton = bitarray32(thrust)
    ron = bitarray32(rot)
    for i in range(0,5):
        wp.digitalWrite(tpins[i],ton[i])
        wp.digitalWrite(rpins[i],ron[i])
    print("thrust is: " + str(thrust))
    print("rot is: " + str(rot))
finally:
    db.close()




#for i in range(0,100):
while True:
    measurement = measure_ultra()
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
