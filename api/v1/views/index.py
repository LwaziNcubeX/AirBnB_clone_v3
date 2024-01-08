#!/usr/bin/python3
"""Add status API endpoint for index page."""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def return_json():
    """
    returns a JSON response with status 'OK'.
    """
    data = {"status": "OK"}
    return jsonify(data)


@app_views.route('/stats', methods=['GET'])
def get_statistics():
    """
    Retrieve the number of each object type.
    """
    data = {
        "amenities": storage.count['Amenity'],
        "cities": storage.count['City'],
        "places": storage.count['Place'],
        "reviews": storage.count['Review'],
        "states": storage.count['State'],
        "users": storage.count['User']
    }
    return jsonify(data)
