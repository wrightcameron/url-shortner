from flask import Flask

from database.db import initialize_db
from flask_restful import Api
from resources.errors import errors

app = Flask(__name__)

from resources.routes import initialize_routes

api = Api(app, errors=errors)

initialize_db(app)
initialize_routes(api)

# running the server
if __name__ == "__main__":
    app.run(debug = True)
