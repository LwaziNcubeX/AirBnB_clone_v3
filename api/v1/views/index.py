from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def json_example():
    data = {"status": "OK"}
    return jsonify(data)
