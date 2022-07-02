
import bcrypt

from engine.mysql import mysql_connection_pool
from models.user import UserModel


class UserService:

    @staticmethod
    def get_user_info(user_id):
        session = mysql_connection_pool.get_connection()
        user_info = UserModel.get_user_info(session=session, user_id=user_id)
        session.close()
        if user_info is None:
            raise Exception("유효하지 않은 회원 입니다.")
        return user_info

    @staticmethod
    def create_user_info(data):
        encrypted_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt())
        data['password'] = encrypted_password
        session = mysql_connection_pool.get_connection()
        UserModel.create_user(session=session, data=data)
        session.close()
        return True

    @staticmethod
    def check_user_validation(data):
        session = mysql_connection_pool.get_connection()
        user_info = UserModel.get_user_info(session=session, email=data['email'])
        if user_info is None:
            raise Exception("유효하지 않은 회원 입니다.")
        check_password = bcrypt.checkpw(data['password'].encode('utf-8'), user_info.password.encode('utf-8'))
        if check_password is False:
            raise Exception('비밀번호가 유효하지 않습니다.')
        session.close()
        return True
