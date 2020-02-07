from flask import Flask, Blueprint, flash, request, redirect, url_for, render_template
from flask_cors import CORS
from backend.config import dev_config
from werkzeug.utils import secure_filename
import os

APP = Flask(__name__)
mod = Blueprint('/fileman', __name__)

dev_config(APP)
CORS(APP)

@mod.route('/upload', methods=['GET', 'POST'])
def upload():
    return 'Upload pic here'