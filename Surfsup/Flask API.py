# Import the dependencies.
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import os

# Database Setup
#engine = create_engine("sqlite:///hawaii.sqlite")

# Define the directory and database filename separately
directory = "/Users/marvinalarry/Documents/Education/Tulsa Community College/Data Visualization/Homework/Challenge #10 - Grade_WIP/sqlalchemy-challengeMarvinaLarry/Surfsup/Resources"
db_filename = "hawaii.sqlite"

# Combine them to create the full database file path
db_file_path = os.path.join(directory, db_filename)

# Create an SQLAlchemy engine object
engine = create_engine(f"sqlite:///{db_file_path}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save references to each table
measurements = Base.classes.measurement
stations = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#Import Flask
from flask import Flask

# Create an app
app = Flask(__name__)

# Define static routes
@app.route("/")
def homepage():
    return "Welcome to the State of Hawaii's Homepage"


@app.route("/about")
def about():
    name = "State of Hawaii"
    location = "Pacific Southwest"

    return f"This website is all about the {name}, and it is positionally located in the {location} region of the United States."


@app.route("/contact")
def contact():
    email = "Hawaii@example.com"

    return f"Questions or Comments? Email an Aloha to {email}."

if __name__ == '__main__':
    app.run()
