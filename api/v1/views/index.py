from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def json_example():
    """
    returns a JSON response with status 'OK'.
    """
    data = {"status": "OK"}
    return jsonify(data)
