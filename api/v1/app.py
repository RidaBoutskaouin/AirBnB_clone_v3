#!/usr/bin/python3
"""This module contains the Flask App"""
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear(self):
    """tear down the app"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Return a 404 error"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    if getenv('HBNB_API_HOST') is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv('HBNB_API_HOST')

    if getenv('HBNB_API_PORT') is None:
        HBNB_API_PORT = '5000'
    else:
        HBNB_API_PORT = getenv('HBNB_API_PORT')

    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
