from flask import Flask, Blueprint, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from .config import dev_config

APP = Flask(__name__)
dev_config(APP)

mongo = PyMongo(APP)
CORS(APP)

mod = Blueprint('/location_form', __name__)

@mod.route('/')
def location_form():
    return '''
        <form method="POST" action="/location_form/create" enctype="multipart/form-data">
            <h2>Location input form</h2>
            <hr>
            Location name:
            <input type="text" name="location"><br>
            Latitude:
            <input type="number" name="latitude" step="0.000001"><br>
            Longitude:
            <input type="number" name="longitude" step="0.000001"><br>
            Description of the location:<br>
            <input type="text" name="description"><br><br>
            <input type="submit">
        </form>
    '''

@mod.route('/create', methods=['POST'])
def create():
    locations = mongo.db.locations
    if request.form.get('location') != '':
            if request.form.get('latitude') != '':
                    if request.form.get('longitude') != '':
                        locations.insert({
                            'location': request.form.get('location'),
                            'coordinates': 
                            {
                                'latitude': request.form.get('latitude'), 
                                'longitude': request.form.get('longitude'),
                            },
                            'description': request.form.get('description')
                        })
                    else:
                        return 'Please endter longitude'
            else:
                return 'Please enter latitude'
    else:
        return 'Please enter location name'
    return '''Success!'''

if __name__ == '__main__':
    APP.run(host='0.0.0.0')