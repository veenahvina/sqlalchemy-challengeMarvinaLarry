# Import the dependencies.
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import os
import json
import datetime as dt
import numpy as np

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

# Define the directory and database filename separately
# directory = "/Users/marvinalarry/Documents/Education/Tulsa Community College/Data Visualization/Homework/Challenge #10 - Grade_WIP/sqlalchemy-challengeMarvinaLarry/Surfsup/Resources"
# db_filename = "hawaii.sqlite"

# # Combine them to create the full database file path
# db_file_path = os.path.join(directory, db_filename)

# # Create an SQLAlchemy engine object
# engine = create_engine(f"sqlite:///{db_file_path}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save references to each table
measurements = Base.classes.measurement
station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)


# Create an app
app = Flask(__name__)

# Define static routes
@app.route("/")
def homepage():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/yyyy-mm-dd<br/>"
        f"/api/v1.0/temp/yyyy-mm-dd/yyyy-mm-dd<br/>"
    )
# Define a precipitation route 
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    precipitation = session.query(measurements.date, measurements.prcp).\
        filter(measurements.date >= prev_year).all()

    session.close()

    precip = {}
    for date, prcp in precipitation:
         precip[date]=precip
    
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Define a stations route 
@app.route("/api/v1.0/stations")
def stations():
    station_Qry = session.query(station.station).all()

    session.close()

    station_list = list(np.ravel(station_Qry))
    return jsonify(station = station_list)

# Define a tobs route 
@app.route("/api/v1.0/tobs")
def tobs():
    last_date_PY = dt.date(2017,8,23)- dt.timedelta(days = 365)
    retrieve_QRY = session.query(measurements.date, measurements.prcp).\
        filter(measurements.date >= last_date_PY).all()
    
    last12tobs_QRY = session.query(measurements.date, measurements.tobs).\
        filter(measurements.date >= last_date_PY).all()
    
    session.close()

    tobs_list = list(np.ravel(last12tobs_QRY))
    return jsonify(tobs = tobs_list)

# Define a start/end route 
@app.route("/api/v1.0/temp/yyyy-mm-dd")
def start():
    HiLowAvg = session.query(func.min(measurements.tobs),func.max(measurements.tobs),func.avg(measurements.tobs)).\
      filter(measurements.date > dt.date(2016,9,8)).all()

    session.close()

    HiLowAvg_list = list(np.ravel(HiLowAvg))
    return jsonify(start = HiLowAvg_list)


# Define a start/end route 
@app.route("/api/v1.0/temp/yyyy-mm-dd/yyyy-mm-dd")
def SEnd():
    StartEnd = session.query(func.min(measurements.tobs),func.max(measurements.tobs),func.avg(measurements.tobs)).\
      filter(measurements.date >= dt.date(2016,9,8)).filter(measurements.date <= dt.date(2017,7,31)).all()

    session.close()

    StartEnd_list = list(np.ravel(StartEnd))
    return jsonify(SEnd = StartEnd_list)

if __name__ == "__main__":
    app.run(debug=True, port=7000)

        