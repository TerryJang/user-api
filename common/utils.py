import re
import random


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
