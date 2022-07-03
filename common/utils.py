import re
import random

import jwt
from exception import InvalidParam
from settings import CONFIG


class Utils:
    @staticmethod
    def gen_auth_phone_code():
        randint = random.randint(1, 999999)
        return f"{randint:0>6}"

    @staticmethod
    def validate_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not re.fullmatch(regex, email):
            return False

        return True

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            return False
        if re.search('[a-z]', password) is None:
            return False
        if re.search('[0-9]', password) is None:
            return False
        if re.search('[A-Z]', password) is None:
            return False
        if password.isalnum():
            return False

        return True


    @staticmethod
    def encode_token(data):
        return jwt.encode(data, key=CONFIG['token_secret_key'])

    @staticmethod
    def decode_token(token):
        try:
            return jwt.decode(token, key=CONFIG['token_secret_key'], algorithms='HS256')
        except Exception as e:
            raise InvalidParam('토큰이 유효하지 않습니다.')

