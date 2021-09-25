import mysql.connector

mydb = mysql.connector.connect(
  host="drone-db.cba0wbjo4ee3.us-east-2.rds.amazonaws.com",
  user="admin",
  password="drone123!",
  database="bcitdrone"
)

mycursor = mydb.cursor()

min_lat = 75
max_lat = 80
min_lon = 40
max_lon = 43

fetch = f"SELECT * FROM gpstest " \
        f"WHERE (latitude BETWEEN {min_lat} AND {max_lat}) AND " \
        f"(longitude BETWEEN {min_lon} AND {max_lon})"

mycursor.execute(fetch)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
