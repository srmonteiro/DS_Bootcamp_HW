# For reference : http://127.0.0.1:5000/
from flask import Flask

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
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>/<end>"
    )
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

# /api/v1.0/precipitation
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# List all routes that are available.Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    
    precipitation_obs = list(np.ravel(annual_analysis))
    
    return jsonify(precipitation_obs)


# /api/v1.0/stations
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

#/api/v1.0/tobs
#query for the dates and temperature observations from a year from the last data point.
#Return a JSON list of Temperature Observations (tobs) for the previous year.


@app.route("/api/v1.0/tobs")
def tobs():
    
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

# /api/v1.0/<start> and /api/v1.0/<start>/<end>

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>/<end>")
def date():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

if __name__ == "__main__":
    app.run(debug=True)

