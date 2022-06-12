from flask import Blueprint, redirect
from database.models import Link
from mongoengine.errors import DoesNotExist
from routes.errors import LinkDoesNotExist, InternalServerError

bp = Blueprint("Reroute", __name__, url_prefix='')


@bp.route("/<short_url>", methods=("GET",))
def shortUrlRedirect(short_url):
    try:
        link = Link.objects.get(short_url=short_url)
        url = link['url']
        return redirect(url, 302)
    except DoesNotExist:
        raise LinkDoesNotExist
    except Exception:
        raise InternalServerError
