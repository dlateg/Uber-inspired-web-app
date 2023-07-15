from flask import Flask, url_for, redirect, session
from functools import wraps
#from flask_googlemaps import GoogleMaps

#from db import engine, SQLModel

app = Flask(__name__)



# import bookHandler
# import map


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True, use_debugger=True)