from flask import Flask, jsonify
from dotenv import load_dotenv
import sqlite3 as sql

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    # add_cars()
    app.run(host="0.0.0.0", port=5000)
