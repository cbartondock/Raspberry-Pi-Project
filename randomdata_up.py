import MySQLdb
import random
import time
db = MySQLdb.connect("sql5.freesqldatabase.com","sql574954","cM7*lB7!","sql574954")

cursor = db.cursor()
clear = "TRUNCATE TABLE SENSORS"
insertvals = "INSERT INTO SENSORS(GPSLAT,GPSLONG,ULTRA,TIME) VALUES ('{lat}','{lon}','{ultra}','{time}')"
cursor.execute(clear)
for i in range(0,100):
	randlat = 360*(.5-random.random())
	randlong = 360*(.5-random.random())
	randultra = 100*random.random()
	currenttime=time.strftime('%Y-%m-%d %H:%M:%S')
	print("({0},{1},{2})".format(randlat,randlong,randultra))
	try:
		cursor.execute(insertvals.format(lat=randlat,lon=randlong,ultra=randultra,time=currenttime))
		db.commit()
	except:
		print("insert failed")
		db.rollback()
db.close()
