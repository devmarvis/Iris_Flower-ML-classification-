from flask import Flask, jsonify, request
from flask_cors import CORS
import util


app = Flask(__name__)
CORS(app)

@app.route("/classify_flower", methods=["GET", "POST"])
def classify_flower():
    data = request.get_json()

    flower_data = list(data.values())
    response = jsonify(util.classify_flower(flower_data))
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(port=5005)