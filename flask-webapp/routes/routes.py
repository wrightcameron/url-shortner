from routes import Link, Reroute, shortUrl
from routes import errors
from flask import jsonify


def initialize_routes(app) -> None:
    """Register blueprint routes with flask app

    Args:
        app (Api): Flask API Instance
    """
    initialize_errors(app)
    app.register_blueprint(Link.bp)
    app.register_blueprint(Reroute.bp)
    app.register_blueprint(shortUrl.bp)


def initialize_errors(app) -> None:
    """Register error handlers

    Args:
        app (Api): Flask API Instance
    """
    @app.errorhandler(errors.ExceptionTest)
    def exception_test(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(errors.InternalServerError)
    def exception_internal_server_error(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(errors.SchemaValidationError)
    def exception_schemaValidationError(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(errors.LinkDoesNotExist)
    def exception_link_does_not_exist(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(errors.LinkAlreadyExistsError)
    def exception_link_already_exists(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(errors.UpdatingLinkError)
    def exception_updating_link_error(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(errors.DeletingLinkError)
    def exception_deleting_link_error(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(errors.UnauthorizedError)
    def exception_unauthorized_error(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(errors.BadTokenError)
    def exception_bad_token_error(e):
        return jsonify(e.to_dict()), e.status_code
