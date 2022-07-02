from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Integer, String, DateTime, func

from common.status_enum import UserStatusEnum

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True, comment='아이디')
    email = Column(String(255), comment='이메일')
    password = Column(String(255), comment='비밀번호')
    status = Column(Integer, comment='유저상태', default=UserStatusEnum.joined.value)
    name = Column(String(255), comment='이름')
    nickname = Column(String(15), comment='닉네임')
    phone = Column(String(255), comment='핸드폰 번호')
    created = Column(DateTime, default=func.now(), comment='생성일')
    updated = Column(DateTime, default=func.now(), onupdate=func.now(), comment='변경일')

    @staticmethod
    def get_user_info(session, user_id=None, email=None):
        query = session.query(UserModel).filter(UserModel.status == UserStatusEnum.joined.value)

        if user_id is not None:
            query = query.filter(UserModel.id == user_id)

        if email is not None:
            query = query.filter(UserModel.email == email)

        return query.first()

    @staticmethod
    def create_user(session, data):
        user = UserModel(**data)
        session.add(user)
        session.commit()
        return True
