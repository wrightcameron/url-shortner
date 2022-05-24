from routes import Link

def initialize_routes(app):
    app.register_blueprint(Link.bp)

# def initialize_routes(api):
#     api.add_resource(LinksApi, '/api/links')
#     api.add_resource(LinkApi, '/api/links/<id>')
