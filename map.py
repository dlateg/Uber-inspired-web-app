from flask import Blueprint, render_template
import database as db
from config import GOOGLE_MAPS_API_KEY
#from main import app

app = Blueprint('map', __name__)


@app.route("/")
def home():
   
   vehicle_list = db.get_drivers()
   return render_template('map.html', vehicles = vehicle_list,api_key=GOOGLE_MAPS_API_KEY)

   
