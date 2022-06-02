from flask import Response, request, Blueprint, redirect
from database.models import Link
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from bson import ObjectId
from routes.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, \
UpdatingMovieError, DeletingMovieError, MovieNotExistsError

bp = Blueprint("Reroute", __name__, url_prefix='')

@bp.route("/<id>", methods=("GET",))
def shortUrlRedirect(id):
    try:
        link = Link.objects.get(id=id)
        url = link['url']
        #TODO If https or http is not included in url, flask thinks this is an internal route.
        return redirect(url, 302)
    except DoesNotExist:
        raise MovieNotExistsError
    except Exception:
        raise InternalServerError
