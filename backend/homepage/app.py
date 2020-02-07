from flask import Flask, render_template, url_for, request, session, redirect, Blueprint
from flask_pymongo import PyMongo
from flask_cors import CORS
from backend.config import dev_config

APP = Flask(__name__)
dev_config(APP)

mongo = PyMongo(APP)
CORS(APP)

mod = Blueprint('/', __name__)

@mod.route('/map')
def homepage():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return 'This is map page'

@mod.route('/about')
def info():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return 'This is info page'