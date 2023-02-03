from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash
from flask_app import app
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,255}$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('swizzle_schema').query_db(query)
        all_users = []
        for user in results:
            all_users.append( cls(user) )
        return all_users

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('swizzle_schema').query_db(query, data)
        if results:
            one_user = cls(results[0])
            return one_user
        return []

    @classmethod
    def get_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('swizzle_schema').query_db(query, data)
        if results:
            this_email = cls(results[0])
            return this_email
        return False



# ---------------------- saves registration data
    @classmethod
    def save_data(cls, data):
        query = '''
            INSERT INTO users( first_name, email, password )
            VALUES( %(first_name)s, %(email)s, %(password)s );
        '''
        return connectToMySQL('swizzle_schema').query_db(query, data)


    @staticmethod
    def validate(form):
        is_valid = True
        if not NAME_REGEX.match(form['first_name']):
            flash(u'First name must be at least 2 characters', 'register_firstname')
            is_valid = False
        if not EMAIL_REGEX.match(form['email']):
            flash(u'Email is not valid', 'register_email')
            is_valid = False
        else:
            all_emails = {
                'email' : form['email']
            }
            if User.get_email(all_emails):
                flash(u'Email already exists', 'register_email')
                is_valid = False
        if not PASSWORD_REGEX.match(form['password']):
            flash(u'Password must contain: minimum eight characters, at least one upper case English letter, one lower case English letter, one number and one special character', 'register_password')
            is_valid = False
        elif not form['password'] == form['confirm']:
            flash(u'Passwords do not match', 'register_confirm_password')
            is_valid = False
        return is_valid