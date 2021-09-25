from flask import Flask
from mysql_connect import fetch_image_uri

app = Flask(__name__)


@app.route("/bcit/drone/data/get/image/longitude/from/<int:from_long>/to/"
           "<int:to_long>/latitude/from/<int:from_lat>/to/<int:to_lat>")
def fetch_image(from_long, to_long, from_lat, to_lat):
    fetch_image_uri(from_long, to_long, from_lat, to_lat)
    return [from_long, to_long, from_lat, to_lat]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
