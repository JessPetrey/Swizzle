from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models.users_model import User
from flask_app.models.drinks_model import Drink
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#?-------------------dynamic home page
@app.route('/')
@app.route('/swizzle')
def index():
    return render_template('index.html')


#? --------------------Login and SignUp forms page
@app.route('/swizzle/forms')
def forms():
    return render_template('login.html')


# ?----------- register a new user
@app.route('/swizzle/register', methods= ['POST'])
def register():
    if not User.validate(request.form):
        # -----------if not valid, redirect to forms
        return redirect('/swizzle/forms')
    #  -------------if valid, get data from form and hash password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['first_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    #-------- create User instance using form data
    user_id = User.save_data(data)
    # --------- store created user's id in session
    session['user_id'] = user_id
    # -------- take the new user to their personalized page
    return redirect(f'/swizzle/{user_id}')

#? ------------login an existing user
@app.route('/swizzle/login', methods=['POST'])
def login():
    # ---------------- validation checks for email and password
    user_in_db = User.get_email(request.form)
    if not user_in_db:
        flash(u'Invalid Email', 'login_email')
        return redirect('/swizzle/forms')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash(u'Incorrect Password', 'login_password')
        return redirect('/swizzle/forms')
    # -------------- if user login inputs are valid, store the user's id in session
    session['user_id'] = user_in_db.id
    id = session['user_id']
    # ------------- take the user to their personalized page
    return redirect(f'/swizzle/{id}')

# ?------------- User's personalized page
@app.route('/swizzle/<int:id>')
def welcome_user(id):
    #? route gaurd ------ if an id is not stored in session, redirect to home page
    if 'user_id' not in session:
        return redirect('/swizzle')
    # -------- if an id is in session, 
    data =  {
        'id' : session['user_id'] 
    }
    user_id = User.get_one(data)
    return render_template('users_page.html', user_id=user_id)

@app.route('/swizzle/list')
def userlist():
    #? route gaurd ------ if an id is not stored in session, redirect to home page
    if 'user_id' not in session:
        return redirect('/swizzle')
    # -------- if an id is in session, 
    data =  {
        'id' : session['user_id'] 
    }
    user_id = User.get_one(data)
    drink_list = Drink.get_all_drinks()
    return render_template('users_list.html', user_id=user_id, drink_list=drink_list)

@app.route('/swizzle/logout')
def end_session():
    session.clear()
    return redirect('/swizzle')