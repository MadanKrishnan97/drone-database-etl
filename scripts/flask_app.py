from flask import Flask
from mysql_connect import fetch_uris
from upload_to_s3 import uri_to_url

app = Flask(__name__)

@app.route("/bcit/drone/data/get/image/longitude/from/<from_long>/to/<to_long>/latitude/from/<from_lat>/to/<to_lat>")
def fetch_image(from_long, to_long, from_lat, to_lat):
    # fetch_from_db(from_long, to_long, from_lat, to_lat)
    s3Uris = fetch_uris(from_lat, to_lat, from_long, to_long)
    s3URLs = uri_to_url(s3Uris)
    return {"urls": s3Uris}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)