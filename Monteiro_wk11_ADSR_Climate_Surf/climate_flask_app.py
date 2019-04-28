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
    )
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

# /api/v1.0/precipitation
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# List all routes that are available.Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    
# Identify Last Date, so you can find 1 year earlier

    results = session.query(Measurement.id, Measurement.station, Measurement.date, Measurement.prcp,Measurement.tobs).\
    order_by(Measurement.date.desc()).all()

# Calculate the date 1 year ago from the last data point in the database
    last_date = [result[2] for result in results[:1]]
    last_day = dt.datetime.strptime(last_date[0], "%Y-%m-%d")
    one_year = dt.timedelta(days=365)
    year_ago = last_day - one_year

    last_year_precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_ago).\
        order_by(Measurement.date.desc()).all()
        
    precipitation_obs = list(np.ravel(last_year_precipitation))
    
    return jsonify(precipitation_obs)


# /api/v1.0/stations
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    
    stations_list = session.query(Measurement.station,)\
        .group_by(Measurement.station).order_by(func.count(Measurement.id).desc()).all()

    stations = list(np.ravel(stations_list))
    
    return jsonify(stations)

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

    last_year_tobs = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= year_ago).\
        order_by(Measurement.date.desc()).all()
        
    temperature_obs = list(np.ravel(last_year_tobs))
    
    return jsonify(temperature_obs)

# /api/v1.0/<start> and /api/v1.0/<start>/<end>

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start_date>") # /<end_date>")
def date(start_date): # , end_date):

    results = session.query(Measurement.date).order_by(Measurement.date.desc()).all()

    last_date = [result[2] for result in results[:1]]
    last_day = dt.datetime.strptime(last_date[0], "%Y-%m-%d")
    one_year = dt.timedelta(days=365)
    year_ago = last_day - one_year

    last_year_readings = session.query(Measurement.date, Measurement.prcp,Measurement.tobs).\
        filter(Measurement.date >= year_ago).order_by(Measurement.date.desc()).all()
     
    for reading in last_year_readings:
        search_start = reading['date']

        if search_start == start_date:
            print("You're on the right track")

       # TMIN = session.query(func.min(Measurement.tobs)).\
        #    filter(Measurement.date >= start_date).\
         #   order_by(Measurement.date.desc()).all() 

        #TMAX = session.query(func.max(Measurement.tobs)).\
         #   filter(Measurement.date >= start_date).\
          #  order_by(Measurement.date.desc()).all() 

        #TAVG = session.query(func.avg(Measurement.tobs)).\
         #   filter(Measurement.date >= start_date).\
          #  order_by(Measurement.date.desc()).all() 

      #  print(f'Since {start_date} the Temp Low was {TMIN}, the Temp High was {TMAX}, and the Average Temp was {TAVG}')

        else: 
            return jsonify({"Error: Somethings wrong with your search or our engine ¯\_(ツ)_/¯"})

    return jsonify(print('Oh, Hello')), 404


if __name__ == "__main__":
    app.run(debug=True)

