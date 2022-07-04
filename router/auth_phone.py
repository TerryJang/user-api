import logging

from flask import Blueprint, request, make_response, jsonify
from http import HTTPStatus
from serializer.auth_phone import AuthPhoneCreateRequestSchema, AuthPhoneUpdateRequestSchema
from service.auth_phone import AuthPhoneService

auth_phone = Blueprint('auth_phone', __name__, url_prefix='/auth-phone')
logger = logging.getLogger('server')


@auth_phone.route('/', methods=['POST'])
def create_auth_phone_code():
    validated_data = AuthPhoneCreateRequestSchema().load(request.json)
    code = AuthPhoneService.create_auth_phone(validated_data['phone'])
    # TODO : 이메일로 코드 전송
    return make_response(jsonify({'response': {'code': code}}), HTTPStatus.OK)


@auth_phone.route('/', methods=['PATCH'])
def update_auth_phone():
    validated_data = AuthPhoneUpdateRequestSchema().load(request.json)
    AuthPhoneService.validate_auth_phone(phone=validated_data['phone'], code=validated_data['code'])
    return make_response(jsonify({'response': {}}), HTTPStatus.OK)
