from resources.link import LinkApi, LinksApi

def initialize_routes(api):
    api.add_resource(LinksApi, '/api/links')
    api.add_resource(LinkApi, '/api/links/<id>')
