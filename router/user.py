import logging

from flask import Blueprint, request, make_response

from service.user import UserService
from serializer.user import UserInfoResponseSchema, UserSignUpRequestSchema, UserLoginRequestSchema

user = Blueprint('user', __name__, url_prefix='/user')
logger = logging.getLogger('server')


@user.route('/login', methods=['POST'])
def login():
    validated_data = UserLoginRequestSchema().load(request.json)
    UserService.check_user_validation(validated_data)
    # TODO : Token 생성하여 리턴
    return {}


@user.route('/signup', methods=['POST'])
def sign_up():
    validated_data = UserSignUpRequestSchema().load(request.json)
    UserService.create_user_info(validated_data)
    return {}


@user.route('/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    # TODO: token 검증
    user_info = UserService.get_user_info(user_id=user_id)
    response = UserInfoResponseSchema().dump(user_info)
    return make_response(response)


@user.route('/password', methods=['PATCH'])
def update_password():
    pass
