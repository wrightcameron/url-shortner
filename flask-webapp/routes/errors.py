# TODO This is an abstract class so should force it be abstract
class BaseException(Exception):

    def __init__(self, message=None, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

    @property
    def message(self) -> str:
        return self.message

    @message.setter
    def message(self, message: str) -> str:
        self.message = message

    @property
    def status_code(self) -> str:
        return self.status_code

    @status_code.setter
    def status_code(self, status_code: str) -> str:
        self.status_code = status_code


class ExceptionTest(BaseException):
    status_code = 400

    def __init__(self, message="Hello World", status_code=None, payload=None):
        super().__init__(message, status_code, payload)

# TODO 500 errors should return stack traces, they are server errors that
# should be fixed


class InternalServerError(BaseException):
    status_code = 500
    message = "Something went wrong"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class SchemaValidationError(BaseException):
    status_code = 400
    message = "Request is missing required fields"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class LinkDoesNotExist(BaseException):
    status_code = 400
    message = "Link with given id doesn't exist"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class LinkAlreadyExistsError(BaseException):
    status_code = 400
    message = "Link with given id already exists"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class UpdatingLinkError(BaseException):
    status_code = 403
    message = "Updating Link added by other is forbidden"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class DeletingLinkError(BaseException):
    status_code = 403
    message = "Deleting Link added by other is forbidden"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class UnauthorizedError(BaseException):
    # Not used yet, no auth
    status_code = 401
    message = "Invalid username or password"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class BadTokenError(BaseException):
    # Not used yet, no auth
    status_code = 403
    message = "Invalid token"

    def __init__(self, message=message, status_code=None, payload=None):
        super().__init__(message, status_code, payload)
