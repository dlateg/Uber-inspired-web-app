from flask import Flask, flash, jsonify, redirect, render_template, request, session
import sqlite3 as SQL
from geopy.distance import geodesic
from calculatedDistance import calculatedistance
from main import app
import json

@app.route('/findmeataxi', methods=['POST'])
def findmeataxi():
    try:

        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])

        con = SQL.connect("drivers.sqlite")
        con.row_factory = SQL.Row
        cur = con.cursor()
        cur.execute("SELECT vehicle_id, latitude, longitude FROM Drivers")
        rows = cur.fetchall()
        con.close()

        
        for row in rows:
          z= {
          "vehicle_id": row[0],
          "longitude": row[1],
          "latitude": row[2]
           }
          

        shortest_distance = 10000

        if len(rows) == 0:
            return "No Drivers"
    

        for row in z:
            distance = calculatedistance(longitude, latitude, row[1], row[2])
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_driver = row[0]


        con = SQL.connect("drivers.sqlite")
        con.row_factory = SQL.Row
        cur = con.cursor()
        cur.execute("""SELECT * FROM Drivers WHERE vehicle_id = %s """, [nearest_driver])
        vehicle = cur.fetchone()
        con.close()

        available_vehicle = {"vehicle": vehicle}
        return json.dumps(vehicle, indent=0)

    except Exception as e:
        return e

