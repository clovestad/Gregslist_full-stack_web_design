from flask_app import app
from flask import render_template, session, request, redirect, flash, Blueprint, jsonify
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import pprint
from flask_app.models.model_listing import listing

from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/new_listing', methods=['POST'])
def create_listing():
    data = {
        'title' : request.form['title'],
        'description' : request.form['description'],
        'location' : request.form['location'],
        'price' : request.form['price'],
        'user_id' : session['user_id']
    }
    valid=listing.is_valid(data)
    if valid:
        listing.create_listing(data)
        pprint.pprint(data)
        flash('listing added')
        return redirect('/')
    return redirect('/new')

@app.route('/view/<int:id>')
def view(id):
    id={
        'id':id
    }
    return render_template('/view.html',listing= listing.get_by_id(id) )

@app.route('/destroy/<int:id>')
def destroy(id):
    data= {
    'id':id
    }
    listing.destroy(data)
    return redirect ('/')

@app.route('/edit/<int:id>' )
def edit(id):
    id={
        'id':id
    }
    return render_template('/edit.html',listing= listing.get_by_id(id))

@app.route('/update', methods=["POST"])
def update():
    data = {
        'id': request.form['id'],
        'title' : request.form['title'],
        'description' : request.form['description'],
        'location' : request.form['location'],
        'price' : request.form['price'],
        'user_id' : session['user_id']
    }
    valid=listing.is_valid(data)
    if valid:
        listing.update(data)
        pprint.pprint(data)
        flash('Listing Updated')
        return redirect('/')
    return redirect('/login')
#futurefeature to geocode db entries to utilize the leaflet app posting all listings location on leaflet
'''listing_bp = Blueprint('listing', __name__)

@listing_bp.route('/api/locations', methods=['GET'])
def get_locations():
    query = "SELECT id, title, location, latitude, longitude FROM listings WHERE latitude IS NOT NULL AND longitude IS NOT NULL"
    listings = connectToMySQL('gregslist').query_db(query)

    return jsonify(listings)'''



