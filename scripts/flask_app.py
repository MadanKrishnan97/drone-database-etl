from flask import Flask

app = Flask(__name__)

lat =
url_str = f"/images/lat/{lat}/lon/{lon}"

@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
