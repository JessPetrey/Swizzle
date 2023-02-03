from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash
from flask_app import app
from flask_app.models import users_model


class Drink:
    def __init__(self, data):
        self.id = data['id']
        self.drink_name = data['drink_name']
        self.instructions = data['instructions']
        self.ingredient1 = data['ingredient1']
        self.ingredient2 = data['ingredient2']
        self.ingredient3 = data['ingredient3']
        self.ingredient4 = data['ingredient4']
        self.ingredient5 = data['ingredient5']
        self.measurement1 = data['measurement1']
        self.measurement2 = data['measurement2']
        self.measurement3 = data['measurement3']
        self.measurement4 = data['measurement4']
        self.measurement5 = data['measurement5']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mixologist = ''

# ===================== create method
    @classmethod
    def save_drink_data(cls, data):
        query = '''
            INSERT INTO savedDrinks(drink_name, instructions, ingredient1,ingredient2,ingredient3,ingredient4,ingredient5,measurement1,measurement2,measurement3,measurement4,measurement5, user_id)
            VALUES(%(drink_name)s, %(instructions)s, %(ingredient1)s,%(ingredient2)s,%(ingredient3)s,%(ingredient4)s,%(ingredient5)s, %(measurement1)s,%(measurement2)s,%(measurement3)s,%(measurement4)s,%(measurement5)s, %(user_id)s);
        '''
        return connectToMySQL('swizzle_schema').query_db(query, data)


# ==================== read all
    @classmethod
    def get_all_drinks(cls):
        query = '''
            SELECT * FROM drinks 
            JOIN users 
            ON drinks.user_id = users.id;
        '''
        results = connectToMySQL('swizzle_schema').query_db(query)
        # print(results)
        all_drinks = []
        if results:
            for row in results:
                this_drink = cls(row)
                user_data = {
                    **row,
                    'id' : row['users.id'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
                this_user = users_model.User(user_data)
                this_drink.mixologist = this_user
                all_drinks.append(this_drink)
        return all_drinks

    @classmethod
    def get_one_drink(cls, data):
        query = '''
            SELECT * FROM drinks
            JOIN users
            ON drinks.user_id = users.id
            WHERE drinks.id = %(id)s;
        '''
        results = connectToMySQL('swizzle_schema').query_db(query, data)
        if results:
            this_drink = cls(results[0])
            row = results[0]
            user_data = {
                **row, 
                'id' : row['users.id'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            this_user = users_model.User(user_data)
            this_drink.mixologist = this_user
            return this_drink
        return False

    # @classmethod
    # def update(cls, data):
    #     query = '''
    #         UPDATE savedDrinks
    #         SET 
    #         name = %(drink_name)s,
    #         description = %(description)s, 
    #         instructions = %(instructions)s, 
    #         date_made = %(date_made)s, 
    #         under_30 = %(under_30)s
    #         WHERE id = %(id)s;
    #     '''
    #     return connectToMySQL('recipes_schema').query_db(query, data)

    # @classmethod
    # def delete(cls, data):
    #     query = '''
    #         DELETE FROM recipes
    #         WHERE id = %(id)s;
    #     '''
    #     return connectToMySQL('recipes_schema').query_db(query, data)


    # @staticmethod
    # def valid_recipe(data):
    #     is_valid = True
    #     if len(data['name']) < 3:
    #         flash(u'Name must be at least 3 characters', 'name')
    #         is_valid = False
    #     if len(data['description']) < 3:
    #         flash(u'Description must be at least 3 characters', 'description')
    #         is_valid = False
    #     if len(data['instructions']) < 3:
    #         flash(u'Instructions must be at least 3 characters', 'instructions')
    #         is_valid = False
    #     if 'under_30' not in data:
    #         is_valid = False
    #         flash(u'Under 30 minutes is required', 'under_30')
    #     if len(data['date_made']) < 1:
    #         is_valid = False
    #         flash(u'Please provide a date', 'date')
    #     return is_valid

            
