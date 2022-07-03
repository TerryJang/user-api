from http import HTTPStatus

from flask import request, make_response, jsonify
from marshmallow import ValidationError


class BaseErrorHandler(Exception):
    status_code = ''
    reason = ''
    request_url = ''

    def to_dict(self):
        return {'reason': self.reason, 'request': self.request_url}


class InvalidParam(BaseErrorHandler):
    def __init__(self, reason, status_code=None):
        self.status_code = HTTPStatus.BAD_REQUEST if not status_code else status_code
        self.reason = reason
        self.request_url = '{} {}'.format(request.method, request.full_path)


class AlreadyExist(BaseErrorHandler):
    def __init__(self, reason, status_code=None):
        self.status_code = HTTPStatus.CONFLICT if not status_code else status_code
        self.reason = reason
        self.request_url = '{} {}'.format(request.method, request.full_path)


class NotFoundContent(BaseErrorHandler):
    def __init__(self, reason, status_code=None):
        self.status_code = HTTPStatus.NOT_FOUND if not status_code else status_code
        self.reason = reason
        self.request_url = '{} {}'.format(request.method, request.full_path)


class InvalidAuthentication(BaseErrorHandler):
    def __init__(self, reason, status_code=None):
        self.status_code = HTTPStatus.UNAUTHORIZED if not status_code else status_code
        self.reason = reason
        self.request_url = '{} {}'.format(request.method, request.full_path)


class ServerError(BaseErrorHandler):
    def __init__(self, reason, status_code=None):
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR if not status_code else status_code
        self.reason = reason
        self.request_url = '{} {}'.format(request.method, request.full_path)


def register_error_handler(app):
    @app.errorhandler(InvalidParam)
    def handle_error(error):
        return make_response(jsonify(error.to_dict()), error.status_code)

    @app.errorhandler(NotFoundContent)
    def handle_error(error):
        return make_response(jsonify(error.to_dict()), error.status_code)

    @app.errorhandler(InvalidAuthentication)
    def handle_error(error):
        return make_response(jsonify(error.to_dict()), error.status_code)

    @app.errorhandler(ServerError)
    def handle_error(error):
        return make_response(jsonify(error.to_dict()), error.status_code)

    @app.errorhandler(ValidationError)
    def handle_error(error):
        if error.messages.get('_schema') is not None:
            return make_response(jsonify({'reason': error.messages['_schema'][0]}), HTTPStatus.BAD_REQUEST)

        return make_response(jsonify({'reason': "요청 정보가 올바르지 않습니다."}), HTTPStatus.BAD_REQUEST)


DEFINED_EXCEPTIONS = (
    AlreadyExist,
    InvalidAuthentication,
    InvalidParam,
    NotFoundContent,
    ServerError,
)