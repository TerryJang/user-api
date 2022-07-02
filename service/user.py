import bcrypt

from engine.mysql import mysql_connection_pool
from models.user import UserModel
from exception import InvalidParam, ServerError


class UserService:
    @staticmethod
    def get_user_info(user_id):
        session = mysql_connection_pool.get_connection()
        try:
            user_info = UserModel.get_user_info(session=session, user_id=user_id)
            if user_info is None:
                raise InvalidParam("회원정보가 유효하지 않습니다.")
            return user_info

        except Exception as e:
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()

    @staticmethod
    def create_user_info(data):
        session = mysql_connection_pool.get_connection()
        try:
            encrypted_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt())
            data['password'] = encrypted_password
            UserModel.create_user(session=session, data=data)
            return True

        except Exception as e:
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.commit()
            session.close()

    @staticmethod
    def check_user_validation(data):
        session = mysql_connection_pool.get_connection()
        try:
            user_info = UserModel.get_user_info(session=session, email=data['email'])
            if user_info is None:
                raise InvalidParam("회원정보가 유효하지 않습니다.")
            check_password = bcrypt.checkpw(data['password'].encode('utf-8'), user_info.password.encode('utf-8'))
            if check_password is False:
                raise InvalidParam('비밀번호가 유효하지 않습니다.')

            return True

        except Exception as e:
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.commit()
            session.close()

