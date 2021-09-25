import mysql.connector

mydb = mysql.connector.connect(
  host="drone-db.cba0wbjo4ee3.us-east-2.rds.amazonaws.com",
  user="admin",
  password="drone123!",
  database="bcitdrone"
)

def fetch_uris(min_lat, max_lat, min_lon, max_lon):

  mycursor = mydb.cursor()


  fetch = f"SELECT * FROM gpstest " \
          f"WHERE (latitude BETWEEN {min_lat} AND {max_lat}) AND " \
          f"(longitude BETWEEN {min_lon} AND {max_lon})"

  mycursor.execute(fetch)

  myresult = mycursor.fetchall()

  s3Uris = [x[3] for x in myresult]

  return s3Uris
