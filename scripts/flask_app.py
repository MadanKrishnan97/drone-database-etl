from flask import Flask

app = Flask(__name__)

@app.route("/bcit/drone/data/get/image/longitude/from/<from_long>/to/<to_long>/latitude/from/<from_lat>/to/<to_lat>")
def fetch_image(from_long, to_long, from_lat, to_lat):
    # fetch_from_db(from_long, to_long, from_lat, to_lat)
    return to_lat


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)