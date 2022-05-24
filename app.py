from flask import Flask

from database.db import initialize_db

app = Flask(__name__)

from routes.routes import initialize_routes

initialize_db(app)
initialize_routes(app)

# running the server
if __name__ == "__main__":
    app.run(debug = True)
