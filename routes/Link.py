from flask import Response, request, Blueprint
from database.models import Link
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from routes.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, \
UpdatingMovieError, DeletingMovieError, MovieNotExistsError


bp = Blueprint("Link", __name__, url_prefix="/api/link")

@bp.route("", methods=("GET",))
def getLinks():
    links = Link.objects().to_json()
    return Response(links, mimetype="application/json", status=200)

#TODO Find what datatype that the ids for mongo are so we can cast.
@bp.route("<id>", methods=("GET",))
def getUniqueLinks(id):
    try:
        links = Link.objects.get(id=id).to_json()
        return Response(links, mimetype="application/json", status=200)
    except DoesNotExist:
        raise MovieNotExistsError
    except Exception:
        raise InternalServerError


@bp.route("", methods=("POST",))
def postLink():
    try:
        body = request.get_json()
        link = Link(**body)
        link.create_short_url()
        link.save()
        id = link.id
        return {'id': str(id)}, 200
    except (FieldDoesNotExist, ValidationError):
        raise SchemaValidationError
    except NotUniqueError:
        raise MovieAlreadyExistsError
    except Exception as e:
        raise InternalServerError

@bp.route("/<id>", methods=("PUT",))
def putLink(id):
    try:
        body = request.get_json()
        Link.objects.get(id=id).update(**body)
        return '', 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingMovieError
    except Exception:
        raise InternalServerError 

@bp.route("/<id>", methods=("DELETE",))
def deleteLink(id):
    try:
        link = Link.objects.get(id=id)
        link.delete()
        return '', 200
    except DoesNotExist:
        raise DeletingMovieError
    except Exception:
        raise InternalServerError
