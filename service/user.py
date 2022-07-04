import bcrypt

from engine.mysql import mysql_connection_pool
from models.user import UserModel
from models.auth_phone import AuthPhoneModel
from exception import InvalidParam, ServerError, DEFINED_EXCEPTIONS


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
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.close()

    @staticmethod
    def create_user_info(data):
        session = mysql_connection_pool.get_connection()
        try:
            code = data.pop('code')
            user_info = UserModel.get_user_info(session=session, email=data['email'])
            if user_info is not None:
                raise InvalidParam("이미 가입된 이메일 입니다.")

            check_auth_phone(session=session, phone=data['phone'], code=code)
            data['password'] = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            UserModel.create_user(session=session, data=data)
            return True

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
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

            return user_info.id

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.commit()
            session.close()

    @staticmethod
    def update_user_password(data):
        session = mysql_connection_pool.get_connection()
        try:
            user_info = UserModel.get_user_info(session=session, email=data['email'])
            if user_info is None:
                raise InvalidParam("회원정보가 유효하지 않습니다.")

            check_auth_phone(session=session, phone=data['phone'], code=data['code'])
            data['password'] = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt())
            UserModel.update_password(session=session, email=data['email'], password=data['password'])
            return True

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.commit()
            session.close()


def check_auth_phone(session, phone, code):
    auth_phone = AuthPhoneModel.get_auth_phone(session=session, phone=phone)
    if auth_phone is None or auth_phone.is_confirm is False or auth_phone.code != code:
        raise InvalidParam("핸드폰 인증이 완료되지 않았습니다. 완료 후 다시 시도해 주세요.")

    return True