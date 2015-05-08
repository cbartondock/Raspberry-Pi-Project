import wiringpi2 as wp
import MySQLdb
import time
from getch import getch
wp.wiringPiSetupPhys()
readlatest = """SELECT t1.* FROM SENSORS t1
WHERE t1.TIME = (SELECT MAX(t2.TIME) FROM SENSORS t2)"""
rpins = [29,31,33,35,37]
tpins = [12,11,13,15,16]
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
print("\n")
thrust, thrustmax = 0, 31
rot, rotmax = 0, 31
bitarray32 = lambda n: map(int,list("0"*(5-len(bin(n)[2:]))+bin(n)[2:]))
while True:
    key = getch()
    if key =="e":
        db=MySQLdb.connect("sql4.freesqldatabase.com","sql476380","eW4%sG5%","sql476380")
	    time.sleep(.00009)
	    cursor=db.cursor()
	    cursor.execute(readlatest)
	    print("SENSORS: "+str(cursor.fetchone()))
	    db.close()
    if key =="w" and thrust<thrustmax:
        thrust+=1
    if key== "s" and thrust>0:
        thrust-=1
    if key =="d" and rot<rotmax:
        rot+=1
    if key=="a" and rot>0:
        rot-=1
    ton = bitarray32(thrust)
    ron = bitarray32(rot)
    for i in range(0,5):
        wp.digitalWrite(tpins[i],ton[i])
        wp.digitalWrite(rpins[i],ron[i])
    print("thrust is: " + str(thrust))
    print("rot is: " + str(rot))
