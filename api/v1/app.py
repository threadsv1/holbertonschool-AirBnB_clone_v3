#!/usr/bin/python3
""" Status of your API """

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(self):
    """Close down current session."""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Return a JSON-formatted 404 status code response."""
    return (jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    hosts = getenv('HBNB_API_HOST', default='0.0.0.0')
    ports = getenv('HBNB_API_PORT', default=5000)
    app.run(host=hosts, port=ports, threaded=True)
    
