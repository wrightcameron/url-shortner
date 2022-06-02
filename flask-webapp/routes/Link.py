from flask import Response, request, Blueprint
from database.models import Link
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from bson import ObjectId
from routes.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, \
UpdatingMovieError, DeletingMovieError, MovieNotExistsError

def sanitizeUrl(url: str) -> str:
    #TODO This needs alot more work, use regex cause there are alot of bed cases for this.
    if 'https' not in url or 'http' not in url:
        url = f"https://{url}"
    return url

bp = Blueprint("Link", __name__, url_prefix="/api/link")

@bp.route("", methods=("GET",))
def getLinks():
    links = Link.objects().to_json()
    return Response(links, mimetype="application/json", status=200)

@bp.route("<id>", methods=("GET",))
def getUniqueLinks(id: ObjectId):
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
        if 'url' in body:
            body['url'] = sanitizeUrl(body['url'])
        link = Link(**body)
        link.create_short_url()
        link.save()
        id = link.id
        # TODO Move the domain name to a env variable that can be read the fastest.
        return {'id': str(id), 'link': f'http://localhost:5000/{str(id)}'}, 200
    except (FieldDoesNotExist, ValidationError):
        raise SchemaValidationError
    except NotUniqueError:
        raise MovieAlreadyExistsError
    except Exception as e:
        raise InternalServerError

@bp.route("/<id>", methods=("PUT",))
def putLink(id: ObjectId):
    try:
        body = request.get_json()
        if 'url' in body:
            body['url'] = sanitizeUrl(body['url'])
        Link.objects.get(id=id).update(**body)
        return '', 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingMovieError
    except Exception:
        raise InternalServerError 

@bp.route("/<id>", methods=("DELETE",))
def deleteLink(id: ObjectId):
    try:
        link = Link.objects.get(id=id)
        link.delete()
        return '', 200
    except DoesNotExist:
        raise DeletingMovieError
    except Exception:
        raise InternalServerError
