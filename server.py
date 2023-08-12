from flask import Flask, request, abort 
from config import me, db
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
    all_cats = []
    cursor = db.products.find({})
    for products in cursor: 
        category = products["category"]
        if category not in all_cats:
            all_cats.append(products["category"])
    return json.dumps (all_cats)

def fix_id(record):
    record["_id"] = str(record ["_id"])
    return record

@app.get("/api/products")
def get_products():
    products = []
    cursor = db.products.find({})
    for product in cursor: 
        products.append(fix_id(product))

    return json.dumps(products)


@app.post("/api/products")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    print(product)
    return json.dumps(fix_id(product))

@app.get("/api/products/category/<cat>")
def get_by_category(cat):
    products = []
    cursor = db.products.find({"category": cat})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

@app.get("/api/reports/total")
def total_value():
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        total += prod["price"]

    return json.dumps(f"The total value is ${total}")

















#start server
app.run(debug=True)
