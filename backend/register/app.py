from flask import Flask, render_template, url_for, request, session, redirect, Blueprint
from flask_pymongo import PyMongo
from flask_cors import CORS
from .config import dev_config
from flask_hashing import Hashing
import hashlib

mod = Blueprint('/register', __name__)

APP = Flask(__name__)
dev_config(APP)

mongo = PyMongo(APP)
CORS(APP)

@mod.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            hashpass = hashlib.sha256(bytes(request.form['pass'], "UTF-8")).hexdigest()
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'Registered!'

    return render_template('register.html')

if __name__ == '__main__':
    APP.run(host='0.0.0.0')