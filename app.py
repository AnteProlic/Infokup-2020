from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from flask_bcrypt import bcrypt
from flask_cors import CORS
from .config import dev_config

APP = Flask(__name__)
dev_config(APP)

mongo = PyMongo(APP)
CORS(APP)

@APP.route('/')
def index():
    print(str(mongo.db))
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('index.html')

@APP.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@APP.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username alrady exists!'

    return render_template('register.html')

if __name__ == '__main__':
    APP.run(host='0.0.0.0')