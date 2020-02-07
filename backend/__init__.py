from flask import Flask

app = Flask(__name__)

from backend.login.app import mod
from backend.register.app import mod
from backend.location_form.app import mod
from backend.homepage.app import mod
from backend.fileman.app import mod

app.register_blueprint(login.app.mod, url_prefix='/users')
app.register_blueprint(register.app.mod, url_prefix='/users')
app.register_blueprint(location_form.app.mod, url_prefix='/location')
app.register_blueprint(homepage.app.mod, url_prefix='/homepage')
app.register_blueprint(fileman.app.mod, url_prefix='/fileman')