from flask import Flask, render_template, url_for, request, session, redirect, Blueprint
from flask_pymongo import PyMongo
from flask_cors import CORS
from .config import dev_config

APP = Flask(__name__)
dev_config(APP)

mongo = PyMongo(APP)
CORS(APP)

mod = Blueprint('/homepage', __name__)

@mod.route('/')
def homepage():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return 'This is homepage'