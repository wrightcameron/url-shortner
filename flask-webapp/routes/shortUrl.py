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


bp = Blueprint("ShortURL", __name__, url_prefix="/api/shortUrl")

@bp.route("<shortUrl>", methods=("GET",))
def getUniqueLinks(shortUrl: ObjectId):
    try:
        if id is None:
            # TODO CHange this to the correct error code
            abort(ExceptionTest.status_code, description="short url needed")
        # If the id is called random, get a random link
        if id == "random":
            links = choice(Link.objects.all()).to_json()
        else:
            links = Link.objects.get(short_url=shortUrl).to_json()
        return Response(links, mimetype="application/json", status=200)
    except (ValidationError, InvalidId):
        raise LinkDoesNotExist()
    except Exception:
        raise InternalServerError()
