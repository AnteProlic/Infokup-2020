from flask import Flask, render_template, url_for, request, session, redirect, Blueprint
from flask_pymongo import PyMongo
from flask_hashing import Hashing
from flask_cors import CORS
from .config import dev_config
import base64
import hashlib

mod = Blueprint('/login', __name__)

APP = Flask(__name__)
dev_config(APP)

mongo = PyMongo(APP)
CORS(APP)
hashing = Hashing(APP)


@mod.route('/login')
def index():
    print(str(mongo.db))
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('index.html')

@mod.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if hashlib.sha256(bytes(request.form['pass'], 'UTF-8')) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    else:
        return 'Invalid username/password combination'
    
    return "Job's done!"

    
if __name__ == '__main__':
    APP.run(host='0.0.0.0')