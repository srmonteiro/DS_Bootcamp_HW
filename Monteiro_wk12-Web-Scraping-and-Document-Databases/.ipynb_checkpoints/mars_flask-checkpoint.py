from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape_app

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_news_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_news=mars_news_data)


# Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

@app.route("/scrape")
def scrape():

    # Store the return value in Mongo as a Python dictionary.
    mars_dashboard = mars_scrape_app.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_dashboard, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
