from flask import Flask, Blueprint, request, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
from backend.config import dev_config

APP = Flask(__name__)
dev_config(APP)

mongo = PyMongo(APP)
CORS(APP)

mod = Blueprint('/location_form', __name__)

@mod.route('/')
def location_form():
    return render_template('location.html')

@mod.route('/add', methods=['POST'])
def add():
    locations = mongo.db.locations
    if request.form.get('location') != '':
            if request.form.get('latitude') != '':
                    if request.form.get('longitude') != '':
                        locations.insert_one({
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


@mod.route('/delete/<location>', methods=['DELETE'])
def delete(location):
    locations = mongo.db.locations
    locations.delete_one({'location': form.get('location')})
    return '''Location Deleted!'''

@mod.route('/put/<location>', methods=['PUT'])
def put(location):
    locations = mongo.db.locations
    locations.update_one({'location': form.get('location')})
    return '''Location Deleted!'''

@mod.route('/get/<location>', methods=['GET'])
def get(location):
    locations = mongo.db.locations
    locations.find_one({'location': form.get('location')})
    return '''Location Deleted!'''

if __name__ == '__main__':
    APP.run(host='0.0.0.0')