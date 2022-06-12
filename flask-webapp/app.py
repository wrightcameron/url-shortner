import os
from flask import Flask
from routes.routes import initialize_routes
from database.db import initialize_db
from flask import abort, jsonify

import traceback
import json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# MongoDB Config settings
app.config['MONGODB_SETTINGS'] = {
    'db': 'url-shortner',
    'host': 'localhost',
    'port': 27017
}

if 'MONGODB_HOSTNAME' in os.environ:
    app.config['MONGODB_SETTINGS']['host'] = os.environ['MONGODB_HOSTNAME']

# First error handling
# This doesn't do what I want, I want to raise errors in the blueprint
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
        "traceback": traceback.format_exc()
    })
    response.content_type = "application/json"
    return response

# Error handling
class LinkAlreadyExistsError(Exception):
    status_code = 400
    message = "Link with given id doesn't exists"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(LinkAlreadyExistsError)
def invalid_link_already_exist(e):
    return jsonify(e.to_dict()), e.status_code

class LinkNotExistsError(Exception):
    status_code = 400
    message = "Link with given id doesn't exists"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(LinkNotExistsError)
def invalid_link_not_exists(e):
    return jsonify(e.to_dict()), e.status_code


initialize_db(app)
initialize_routes(app)

# running the server
if __name__ == "__main__":
    app.run(debug = False)
