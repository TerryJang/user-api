import logging
from http import HTTPStatus

from flask import Blueprint, request, make_response, jsonify

from service.user import UserService
from serializer.user import UserInfoResponseSchema, UserSignUpRequestSchema, UserLoginRequestSchema, UserUpdatePasswordRequestSchema
from common.utils import Utils

user = Blueprint('user', __name__, url_prefix='/user')
logger = logging.getLogger('server')


@user.route('/login', methods=['POST'])
def login():
    validated_data = UserLoginRequestSchema().load(request.json)
    user_id = UserService.check_user_validation(validated_data)
    token = Utils.encode_token({'user_id': user_id})
    return make_response(jsonify({'response': {'token': token}}), HTTPStatus.OK)


@user.route('/signup', methods=['POST'])
def sign_up():
    validated_data = UserSignUpRequestSchema().load(request.json)
    UserService.create_user_info(validated_data)
    return make_response(jsonify({'response': {}}), HTTPStatus.CREATED)


@user.route('/', methods=['GET'])
def get_user_info():
    token = request.headers.get('Authorization')
    decoded_token = Utils.decode_token(token)
    user_info = UserService.get_user_info(user_id=decoded_token['user_id'])
    response = UserInfoResponseSchema().dump(user_info)
    return make_response(jsonify({'response': response}), HTTPStatus.OK)


@user.route('/password', methods=['PATCH'])
def update_password():
    validated_data = UserUpdatePasswordRequestSchema().load(request.json)
    UserService.update_user_password(validated_data)
    return make_response(jsonify({'response': {}}), HTTPStatus.OK)
