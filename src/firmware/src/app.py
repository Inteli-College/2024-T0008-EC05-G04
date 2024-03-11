from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/ping", methods=["GET"])
def ping():
    return "pong"


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return data


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
