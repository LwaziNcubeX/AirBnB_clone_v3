#!/usr/bin/python3
"""
Add Blueprint to Flask app and tick
threaded as true
"""
import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_storage(exception):
    """
    closes the storage when the application context is torn down.
    """
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """create a custom error handler for the 404"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
