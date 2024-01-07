import os
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


def close_storage(exception=None):
    """
    closes the storage when the application context is torn down.
    """
    storage.close()


app.teardown_appcontext(close_storage)


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True, debug=True)