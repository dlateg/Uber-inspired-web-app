from flask import Flask, jsonify
from dotenv import load_dotenv
from database import get_drivers


load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(get_drivers())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
