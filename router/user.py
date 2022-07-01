from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/', methods=['GET'])
def get_user():
    return 'user'


@user.route('/', methods=['POST'])
def create_user():
    pass


@user.route('/password', methods=['PATCH'])
def update_password():
    pass
