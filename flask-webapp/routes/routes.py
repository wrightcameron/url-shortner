from routes import Link, Reroute

def initialize_routes(app):
    app.register_blueprint(Link.bp)
    app.register_blueprint(Reroute.bp)
