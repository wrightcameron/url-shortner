import re
from random import choice
from database.models import Link
from bson import ObjectId
from bson.errors import InvalidId
from flask import abort, Response, request, Blueprint
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, \
    DoesNotExist, ValidationError, InvalidQueryError
from routes.errors import ExceptionTest, LinkDoesNotExist, \
    InternalServerError, SchemaValidationError, LinkAlreadyExistsError, \
    UpdatingLinkError


# TODO Should we include this in the model?  If callable function
# it might make sense
def sanitizeUrl(url: str) -> str:
    if re.search('^https?://', url) is None:
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
        if id is None:
            # TODO CHange this to the correct error code
            abort(ExceptionTest.status_code, description="Id needed")
        # If the id is called random, get a random link
        if id == "random":
            links = choice(Link.objects.all()).to_json()
        else:
            links = Link.objects.get(id=id).to_json()
        return Response(links, mimetype="application/json", status=200)
    except (ValidationError, InvalidId):
        raise LinkDoesNotExist()
    except Exception:
        raise InternalServerError()


@bp.route("", methods=("POST",))
def postLink():
    try:
        body = request.get_json()
        # TODO Check if contents of body are correct
        if 'url' in body:
            body['url'] = sanitizeUrl(body['url'])
        else:
            abort(400)
        link = Link(**body)
        link.create_short_url()
        # link.addCreatedTIme()
        # TODO Mongo has callables like validation and default.
        # Having those be called instead of here would be better.
        link.save()

        short_url = link.short_url
        id = link.id
        # TODO Move the domain name to a env variable that can
        # be read the fastest.
        host = 'http://localhost:5000'
        return {'id': str(id), 'short_url': str(short_url),
                'link': f'{host}/{str(short_url)}'}, 200
    except (FieldDoesNotExist, ValidationError):
        raise SchemaValidationError
    except NotUniqueError:
        raise LinkAlreadyExistsError
    except Exception:
        raise InternalServerError


@bp.route("/<id>", methods=("PUT",))
def putLink(id: ObjectId):
    try:
        body = request.get_json()
        if 'url' in body:
            body['url'] = sanitizeUrl(body['url'])
        Link.objects.get(id=id).update(**body)
        return '', 200
    except (ValidationError, InvalidId):
        raise LinkDoesNotExist()
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingLinkError
    except Exception:
        raise InternalServerError


@bp.route("/<id>", methods=("DELETE",))
def deleteLink(id: ObjectId):
    try:
        link = Link.objects.get(id=id)
        link.delete()
        return '', 200
    except (ValidationError, InvalidId):
        raise LinkDoesNotExist()
    except Exception:
        raise InternalServerError
