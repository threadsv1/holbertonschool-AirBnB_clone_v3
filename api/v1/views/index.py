#!/usr/bin/python3
""" index """

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """Return status in JSON."""
    return jsonify(status="OK")


@app_views.route('/stats')
def stat():
    """Endpoint that retrieves the number of objs by type."""
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    counter = {}
    for s in classes:
        counter[s] = storage.count(classes[s])
    return jsonify(counter)
