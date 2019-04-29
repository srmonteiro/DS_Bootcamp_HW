# For reference : http://127.0.0.1:5000/
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Instructions/Resources/hawaii.sqlite")
conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################


app = Flask(__name__)

# /
# Home page.
# List all routes that are available.

@app.route("/")
def home():
    
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/%start%/%end%<br/>"
        f"/api/v1.0/<start> <br/>"
        f'enter start date as YYYY-MM-DD <br/>'
        f"/api/v1.0/<start>/<end> <br/>"
        f'enter start date as YYYY-MM-DD, "/", and end date as YYY-MM-DD'
    )

# /api/v1.0/precipitation
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# List all routes that are available.Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():

    results = session.query(Measurement.station, Measurement.date, Measurement.prcp).\
    order_by(Measurement.date.desc()).all()

    precipitation_json = []
    for Measurement.date, Measurement.station, Measurement.prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = Measurement.date
        precipitation_dict["station"] = Measurement.station
        precipitation_dict["prcp"] = Measurement.prcp
        precipitation_json.append(precipitation_dict)

    #return jsonify(station_precipitation)
    return jsonify(precipitation_json)


# /api/v1.0/stations
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    
    stations_list = session.query(Station.id, Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()
    
    stations_json = []
    for Station.id, Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation in stations_list:
        station_dict = {}
        station_dict["id"] = Station.id
        station_dict["name"] = Station.name
        station_dict["lat"] = Station.latitude
        station_dict["long"] = Station.longitude
        station_dict["elevation"] = Station.elevation
        stations_json.append(station_dict)
    
    return jsonify(stations_json)

#/api/v1.0/tobs
#query for the dates and temperature observations from a year from the last data point.
#Return a JSON list of Temperature Observations (tobs) for the previous year.


@app.route("/api/v1.0/tobs")
def tobs():
    
    results = session.query(Measurement.id, Measurement.station, Measurement.date, Measurement.prcp,Measurement.tobs).\
    order_by(Measurement.date.desc()).all()

    last_date = [result[2] for result in results[:1]]
    last_day = dt.datetime.strptime(last_date[0], "%Y-%m-%d")
    one_year = dt.timedelta(days=365)
    year_ago = last_day - one_year

    last_year_tobs = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
        filter(Measurement.date >= year_ago).\
        order_by(Measurement.date.desc()).all()

    temps_json = []
    for Measurement.date, Measurement.station, Measurement.tobs in last_year_tobs:
        temp_dict = {}
        temp_dict["date"] = Measurement.date
        temp_dict["station"] = Measurement.station
        temp_dict["temp"] = Measurement.tobs
        temps_json.append(temp_dict)                             
    
    return jsonify(temps_json)

# /api/v1.0/<start> and /api/v1.0/<start>/<end>

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>") # /<end_date>")

# Thank you to Karen Gutzman for coaching me through this syntax! I was so stuck!

def app_start_date(start): # , end_date):

    trip_start = calc_starttemps(start)
    trip_start_list = trip_start[0]
    temp_min = trip_start_list[0]
    temp_avg = trip_start_list[1]
    temp_max = trip_start_list[2]
    temp_dict = dict({'Min': temp_min, 'Avg': temp_avg, 'Max': temp_max })

    return jsonify(temp_dict)

def calc_starttemps(start_date):
      
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    """When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` 
    for all dates greater than and equal to the start date."""

    #start_string = dt.strptime(start,'%Y-%m-%d' )
    startend_temps = []
    trip_startend = calc_temps_startend(start, end)
    trip_startend_list = trip_startend[0]
    temp_min = trip_startend_list[0]
    temp_avg = trip_startend_list[1]
    temp_max = trip_startend_list[2]
    temp_dict = dict({'Min Temp': temp_min, 'Max Temp': temp_max, 'Avg Temp' : temp_avg, })
    startend_temps.append(dict(temp_dict))
    
    #return jsonify(temp_dict)
    return jsonify(temp_dict)

def calc_temps_startend(start_date, end_date):
      
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

if __name__ == "__main__":
    app.run(debug=True)

