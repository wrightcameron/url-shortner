from flask import Response, request, Blueprint, redirect
from database.models import Link
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from bson import ObjectId
from routes.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, \
UpdatingMovieError, DeletingMovieError, MovieNotExistsError

bp = Blueprint("Reroute", __name__, url_prefix='')

@bp.route("/<short_url>", methods=("GET",))
def shortUrlRedirect(short_url):
    try:
        link = Link.objects.get(short_url=short_url)
        url = link['url']
        return redirect(url, 302)
    except DoesNotExist:
        raise MovieNotExistsError
    except Exception:
        raise InternalServerError
