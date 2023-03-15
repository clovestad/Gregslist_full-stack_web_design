from flask_app import app
from flask import render_template,redirect, session, request, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.model_user import User 
from flask_app.models.model_listing import listing

@app.route('/')
def index():


    return render_template('home.html', )



@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password']
    }
    valid= User.user_validator(data)
    if valid:
        pw_hash= bcrypt.generate_password_hash(request.form['password'])
        data['pw_hash'] = pw_hash
        user = User.create_user(data)
        session['user_id'] = user
        flash('Account Successfully Created Please Login')
        return redirect('/login')
    return redirect('/login')

@app.route('/login_user', methods= ['POST'])
def login_user():

    user= User.get_by_email(request.form)
    if not user:
        flash('invalid email or password')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('invalid email or password')
        return redirect('/')
    session['user_id']= user.id
    return redirect('/')
##newshit


@app.route("/about")
def about():
    return render_template('about.html' )

@app.route("/search")
def search():
    return render_template('search.html' )

@app.route("/new")
def new():
    return render_template('new.html' )

@app.route("/login")
def logint():
    return render_template('login.html' )

@app.route("/inbox")
def inbox():
    return render_template('inbox.html',)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


