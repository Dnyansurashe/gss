from flask import Flask, render_template, request
from pymongo import MongoClient # type: ignore

app = Flask(__name__)

# MongoDB connection function
def get_db_connection():
    client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
    db = client["grocery_store"]  # Replace 'my_database' with your database name
    return db

# Home route
@app.route('/')
def home():
    return render_template('index.htm')

@app.route('/result')
def result():
    return render_template('result.htm')

# Search route handling both GET and POST

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Get the search query
        query = request.form.get('query')
        
        if not query.strip():
            return render_template('result.htm', items=[], error="Please enter a search term.")
        
        # Search for items in MongoDB
        db = get_db_connection()
        grocery_items_collection = db["grocery_items"]
        items = list(grocery_items_collection.find({"name": {"$regex": query, "$options": "i"}}))  # Case-insensitive search
        
        # Pass the results to the template
        return render_template('result.htm', items=items)
    
    return render_template('search.htm')

@app.route('/shop')
def shop():
    # Fetch grocery items from MongoDB
    db = get_db_connection()
    grocery_items_collection = db["grocery_items"]  # Replace 'grocery_items' with your collection name
    grocery_items = list(grocery_items_collection.find())
    
    # Pass items to the template
    return render_template('shop.htm', items=grocery_items)

# Other pages linked from index.htm
@app.route('/cart')
def cart():
    return render_template('cart.htm')

@app.route('/checkout')
def checkout():
    return render_template('checkout.htm')

@app.route('/shopnow1')
def shopnow1():
    return render_template('shopnow1.htm')

@app.route('/shopnow2')
def shopnow2():
    return render_template('shopnow2.htm')

@app.route('/shopnow3')
def shopnow3():
    return render_template('shopnow3.htm')

@app.route('/shopnow4')
def shopnow4():
    return render_template('shopnow4.htm')

@app.route('/shopnow5')
def shopnow5():
    return render_template('shopnow5.htm')

@app.route('/shopnow6')
def shopnow6():
    return render_template('shopnow6.htm')

@app.route('/readmore')
def readmore():
    return render_template('readmore.htm')

@app.route('/freedelivery')
def freedelivery():
    return render_template('freedelivery.htm')

@app.route('/easypayment')
def easypayment():
    return render_template('easypayment.htm')

@app.route('/process1')
def process1():
    return render_template('process1.htm')

@app.route('/ordertracking')
def ordertracking():
    return render_template('ordertracking.htm')

@app.route('/checkout1')
def checkout1():
    return render_template('checkout1.htm')


@app.route('/pop')
def pop():
    return render_template('pop.htm')

# Add more routes if there are additional files referenced in index.htm

if __name__ == "__main__":
    app.run(debug=True)

