from flask import Response, request
from database.models import Link
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, \
UpdatingMovieError, DeletingMovieError, MovieNotExistsError


class LinksApi(Resource):
    def get(self):
        links = Link.objects().to_json()
        return Response(links, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            link = Link(**body)
            link.save()
            id = link.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise MovieAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class LinkApi(Resource):
    def get(self, id):
        try:
            links = Link.objects.get(id=id).to_json()
            return Response(links, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception:
            raise InternalServerError

    def put(self, id):
        try:
            body = request.get_json()
            Movie.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingMovieError
        except Exception:
            raise InternalServerError       
    
    def delete(self, id):
        try:
            movie = Movie.objects.get(id=id)
            movie.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingMovieError
        except Exception:
            raise InternalServerError
