from common.utils import Utils
from engine.mysql import mysql_connection_pool
from models.auth_phone import AuthPhoneModel
from exception import InvalidParam, ServerError, DEFINED_EXCEPTIONS


class AuthPhoneService:
    @staticmethod
    def create_auth_phone(phone):
        session = mysql_connection_pool.get_connection()
        try:
            code = Utils.gen_auth_phone_code()
            data = {"phone": phone, "code": code}
            AuthPhoneModel.create_auth_phone(session=session, data=data)

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.commit()
            session.close()

        return code

    @staticmethod
    def validate_auth_phone(phone, code):
        session = mysql_connection_pool.get_connection()
        try:
            auth_phone = AuthPhoneModel.get_auth_phone(session=session, phone=phone)
            if auth_phone is None or auth_phone.code != code:
                raise InvalidParam(reason='인증 코드가 유효하지 않습니다. 확인 후 다시 시도해 주세요.')
            if auth_phone.is_confirm is True:
                raise InvalidParam(reason='이미 인증이 완료된 코드 입니다. 인증을 다시 시도해 주세요.')
            AuthPhoneModel.update_auth_phone(session=session, phone=phone, code=code)

        except Exception as e:
            if any([isinstance(e, exc) for exc in DEFINED_EXCEPTIONS]):
                raise e
            raise ServerError(reason='서버 오류가 발생 했습니다.')

        finally:
            session.commit()
            session.close()

        return True
