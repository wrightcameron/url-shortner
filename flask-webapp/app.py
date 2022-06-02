import os
from flask import Flask
from routes.routes import initialize_routes
from database.db import initialize_db

app = Flask(__name__)

# MongoDB Config settings
app.config['MONGODB_SETTINGS'] = {
    'db': 'url-shortner',
    'host': 'localhost',
    'port': 27017
}

if os.environ['MONGODB_HOSTNAME'] is not None:
    app.config['MONGODB_SETTINGS']['host'] = os.environ['MONGODB_HOSTNAME']

initialize_db(app)
initialize_routes(app)

# running the server
if __name__ == "__main__":
    app.run(debug = True)
