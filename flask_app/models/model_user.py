from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL
DB= "gregslist"
class User:
    def __init__(self, data):
        self.id= data['id']
        self.first_name=data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls,user):
        query ="INSERT into users( first_name, last_name, email, password) VALUES ( %(first_name)s,  %(last_name)s , %(email)s ,%(pw_hash)s )"
        result= connectToMySQL(DB).query_db(query,user)
        return result


    @classmethod
    def get_by_email(cls,data):
        query= "SELECT * from users WHERE email = %(email)s"
        results = connectToMySQL(DB).query_db(query,data)
        if len(results) < 1:
            return False
        return(cls(results[0]))

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * from users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data) 


    @staticmethod
    def user_validator(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['first_name']) < 2:
            flash('first name must be at least 2 characters')
            is_valid= False
        if len(data['last_name']) < 3:
            flash('last_name must be at least 3 characters')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('invalid EMAIL')
            is_valid = False
        query= "SELECT * from users WHERE email = %(email)s"
        results = connectToMySQL(DB).query_db(query,data)
        if len(results) != 0:
            flash('this email is already in use')
            is_valid= False
        if len(data['email']) < 2 :
            flash('thats totes not a real email')
            is_valid = False
        if len(data['password']) < 8 :
            flash('password insufficient')
            is_valid= False
        if data['password'] != data['confirm_password']:
            flash('the passwords do not match')
            is_valid = False
        return is_valid 