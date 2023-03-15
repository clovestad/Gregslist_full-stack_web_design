from flask_app import app
from flask import flash
import pprint
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_user import User

DB= "tv_shows"
class listing:
    def __init__(self,data):
        self.id = data['id']
        self.title = data["title"]
        self.network= data["network"]
        self.date = data["date"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.update_at = data["update_at"]
        self.users_id = data["users_id"]
        self.planner= None

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * from shows WHERE id= %(id)s"
        result = connectToMySQL(DB).query_db(query, data)
        pprint.pprint(result)
        return cls(result[0])

    @classmethod
    def get_alls(cls):
        query = "SELECT * from users JOIN shows ON  shows.users_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
        pprint.pprint(results)
        not_farts= []
        for shows in results:
            planner= User(shows)
            shows_data= {
                'id': shows['shows.id'],
        'title' : shows['title'],
        'network' : shows['network'],
        'date' : shows['date'],
        'description' : shows ['description'],
        'created_at': shows['created_at'],
        'update_at': shows['update_at'],
        'users_id' : shows['users_id']
            }
            planner.shows = show(shows_data)
            not_farts.append(planner)
        return  not_farts

    @classmethod
    def create_show(cls, data):
        query = "INSERT into shows (title, network, date, description , users_id ) VALUES (%(title)s, %(network)s, %(date)s, %(description)s, %(users_id)s);"
        result = connectToMySQL(DB).query_db(query, data)
        return result
        

    @classmethod
    def update(cls,data):
        query = "UPDATE shows SET title = %(title)s,network = %(network)s, date = %(date)s, description = %(description)s WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        pprint.pprint(result)
        return result

    @staticmethod
    def is_valid(show):
        valid = True
        if len(show['title']) < 3:
            valid = False
            flash("name must be 3 characters")
        if len(show['network']) < 1:
            valid = False
            flash("netweork invalid")
        if len(show['description']) < 3:
            valid = False
            flash("description must be longer than 3 characters")
        return valid

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data) 