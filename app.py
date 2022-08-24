#The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL
from flask import Flask, render_template, redirect, url_for
# use PyMongo to interact with our Mongo database
from flask_pymongo import PyMongo
# to use the scraping code, we will convert from Jupyter notebook to Python.
import scraping

# set up Flask
app = Flask(__name__)

# tell Python how to connect to Mongo using PyMongo using Flask
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Set Up App Routes (code to set up our Flask routes)
#1 route for main HTML page everyone will view when visiting the web app
#2 route to actually scrape new data using the code we've written

# First define the route for the HTML page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# set up scraping route.  this route will be the "button" of the web app, the
# one the scrapes updated data when we tell it to from the homepage of our web app.
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)

# Tell Flask to run
if __name__ == "__main__":
    app.run()

