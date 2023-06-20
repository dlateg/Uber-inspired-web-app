from flask import Flask, jsonify
#from dotenv import load_dotenv
#from database import get_drivers
from flask import Flask, render_template
import database as db
import json


#load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
   
   vehicle_list = db.get_drivers()
   return vehicle_list
   
   return render_template('map.html', vehicles = vehicle_list)
   

app.static_folder = 'static'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
