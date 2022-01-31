from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data"
mongo = PyMongo(app)




@app.route("/")
def index():
    """doc string - gets one article from mongo db and render to the page"""
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars_index=mars)


@app.route("/scrape")
def scraper():
    """doc string stays on top of the function - scrape Mars article and put in the db - code=302 meaning redirect to the home page"""    
    mars = mongo.db.mars
# define mars_data as a local variable   
# the scrape function call scrape all 
    mars_data = scraping.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
