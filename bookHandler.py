#code adapted from Keith Mannock
from flask import Flask, Blueprint, flash, jsonify, redirect, render_template, request, session, make_response
import sqlite3 as SQL
from calculatedDistance import calculatedistance
from sqlite3 import OperationalError
from config import GOOGLE_MAPS_API_KEY

app = Blueprint('bookHandler', __name__)

@app.route('/findmeataxi', methods=['POST'])
def findmeataxi():
    # try:

        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])

        con = SQL.connect("drivers.sqlite")
        con.row_factory = SQL.Row
        cur = con.cursor()
        cur.execute("SELECT vehicle_id, latitude, longitude FROM driver")
        rows = cur.fetchall()
        con.close()
          

        shortest_distance = 10000

        if len(rows) == 0:
            return "No Drivers"
    

        for row in rows:
            distance = calculatedistance(longitude, latitude, row['longitude'], row['latitude'])
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_driver = row['vehicle_id']


        con = SQL.connect("drivers.sqlite")
        con.row_factory = SQL.Row
        cur = con.cursor()
        cur.execute("SELECT vehicle_id, latitude, longitude FROM driver WHERE vehicle_id = ?", (nearest_driver,))
        vehicle = cur.fetchone()
        cur.close()
        con.close()


        nearest_driver_dict = dict(vehicle)

        print(nearest_driver_dict)

        nearest_driver = jsonify(nearest_driver_dict)

        
        return render_template('book.html',latitude=latitude, longitude=longitude, nearest_driver = nearest_driver_dict, api_key=GOOGLE_MAPS_API_KEY)

        
        
    
    # # except OperationalError as e:
    #     return make_response("An error occurred while processing the request: " + str(e), 500)

    # except Exception as e:
    #     return make_response("An error occurred: " + str(e), 500)
