from engine.mysql import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, func


class AuthPhoneModel(Base):
    __tablename__ = 'auth_phone'

    id = Column(BigInteger, primary_key=True, comment='아이디')
    phone = Column(String(20), nullable=False, comment='핸드폰번호')
    code = Column(String(10), nullable=False, comment='인증코드')
    is_confirm = Column(Boolean, default=False, comment='인증여부')
    created_at = Column(DateTime, default=func.now(), comment='생성일')
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), comment='변경일')

    @staticmethod
    def create_auth_phone(session, data):
        auth_phone = AuthPhoneModel(**data)
        session.add(auth_phone)

    @staticmethod
    def get_auth_phone(session, phone):
        return session.query(AuthPhoneModel).filter(
            AuthPhoneModel.phone == phone,
        ).order_by(AuthPhoneModel.id.desc()).first()

    @staticmethod
    def update_auth_phone(session, phone, code):
        session.query(AuthPhoneModel).filter(
            AuthPhoneModel.phone == phone,
            AuthPhoneModel.code == code).update({"is_confirm": True})
