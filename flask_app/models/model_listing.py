from flask_app import app
from flask import flash
import pprint
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_user import User

DB= "gregslist"
class listing:
    def __init__(self,data):
        self.id = data['id']
        self.title = data["title"]
        self.description = data["description"]
        self.location = data["location"]
        self.price = data["price"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.planner= None

    @staticmethod
    def is_valid(listing):
        valid = True
        if len(listing['title']) < 3:
            valid = False
            flash("Invalid Title")
        if len(listing['description']) < 1:
            valid = False
            flash("Invalid Description")
        if len(listing['location'])<1:
            valid= False
            flash("Invalid Location")
        if len(listing['price'])<1:
            valid= False
            flash("Invalid Price")

        return valid
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * from listings WHERE id= %(id)s"
        result = connectToMySQL(DB).query_db(query, data)
        pprint.pprint(result)
        return cls(result[0])


    @classmethod
    def get_alls(cls):
        query = "SELECT * from users JOIN listings ON  listings.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
##        pprint.pprint(results)
        not_farts= []
        for listings in results:
            planner= User(listings)
            listings_data= {
                'id': listings['listings.id'],
        'title' : listings['title'],
        'description' : listings ['description'],
        'location' : listings['location'],
        'price' : listings['price'],
        'created_at': listings['created_at'],
        'updated_at': listings['updated_at'],
        'user_id' : listings['user_id']
            }
            planner.listings = listing(listings_data)
            not_farts.append(planner)
        return  not_farts

    @classmethod
    def create_listing(cls, data):
        query = "INSERT into listings (title, description ,location,price, user_id ) VALUES (%(title)s, %(description)s,%(location)s,%(price)s, %(user_id)s);"
        result = connectToMySQL(DB).query_db(query, data)
        return result

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM listings WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data) 

    @classmethod
    def update(cls,data):
        query = "UPDATE listings SET title = %(title)s,description = %(description)s,location = %(location)s,price = %(price)s  WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        pprint.pprint(result)
        return result



