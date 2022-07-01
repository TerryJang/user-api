from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Integer, String, DateTime, func

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True, comment='아이디')
    email = Column(String(255), comment='이메일')
    password = Column(String(255), comment='비밀번호')
    status = Column(Integer, comment='유저상태')
    name = Column(String(255), comment='이름')
    nickname = Column(String(15), comment='닉네임')
    phone = Column(String(255), comment='핸드폰 번호')
    created = Column(DateTime, default=func.now(), comment='생성일')
    updated = Column(DateTime, default=func.now(), onupdate=func.now(), comment='변경일')
