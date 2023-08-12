from flask import Flask
from config import me
import json

#creates server
app = Flask("server")

@app.get("/")
def home():
    return "Hello World"

@app.get("/test")
def test():
    return "this is a test page"

@app.get("/about")
def about():
    return "Dottie"


#####################API PRODUCTS
##USE JSON

@app.get("/api/about/developer")
def developer():
    full_name = me["name"] + " " + me["last_name"]
    return json.dumps(full_name)


@app.get("/api/aboutus")
def aboutus_data():
    return json.dumps(me)

@app.get("/api/categories")
def categories():
    all_cats = ["earrings", "boards", "other"]
    return json.dumps (all_cats)



#start server
app.run(debug=True)