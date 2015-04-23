import MySQLdb

db = MySQLdb.connect("sql5.freesqldatabase.com","sql574954","cM7*lB7!","sql574954")

cursor = db.cursor()

readfirst = """
SELECT GPSLAT,GPSLONG,ULTRA,TIME FROM SENSORS
"""
readlast = """
SELECT t1.* FROM SENSORS t1
WHERE t1.TIME = (SELECT MAX(t2.TIME) FROM SENSORS t2)
"""
cursor.execute(readlast)
read = cursor.fetchone()
print("read: ",read)

