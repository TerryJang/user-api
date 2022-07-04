import os
import json
import unittest
from http import HTTPStatus

from sqlalchemy.orm.session import close_all_sessions
from sqlalchemy import BigInteger
from sqlalchemy.ext.compiler import compiles

from main import app
from engine.mysql import mysql_connection_pool, Base
from settings import CONFIG


class UserAPITestCase(unittest.TestCase):

    def setUp(self):
        os.environ['APPLICATION_ENV'] = 'test'
        self.app = app.test_client()

        mysql_connection_pool.setup(CONFIG)
        for table in Base.__subclasses__():
            table.__table__.create(bind=mysql_connection_pool.engine, checkfirst=True)

    @compiles(BigInteger, 'sqlite')
    def compile_BIGINTEGER(element, compiler, **kw):
        return compiler.visit_integer(element, **kw)

    def tearDown(self):
        close_all_sessions()
        Base.metadata.drop_all(bind=mysql_connection_pool.engine)
        del self.app

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status_code == HTTPStatus.OK

    def test_user_info(self):
        token = self.test_login()
        rv = self.app.get(
            path='/user/',
            headers={'Authorization': token},
            content_type='application/json',
        )
        assert rv.status_code == HTTPStatus.OK

    def test_create_auth_code(self):
        res = self.app.post(
            path='/auth-phone/',
            content_type='application/json',
            json={
                'phone': '01012341234'
            })
        assert res.status_code == HTTPStatus.OK
        return res.json['response']['code']

    def test_update_auth_phone(self):
        code = self.test_create_auth_code()

        res = self.app.patch(
            path='/auth-phone/',
            content_type='application/json',
            json={
                'phone': '01012341234',
                'code': code
            }
        )
        assert res.status_code == HTTPStatus.OK
        return code

    def test_signup(self):
        code = self.test_update_auth_phone()

        res = self.app.post(
            path='/user/signup',
            content_type='application/json',
            data=json.dumps({
                'email': 'test@naver.com',
                'password': 'aA12341234!',
                'name': 'test',
                'nickname': 'test',
                'phone': '01012341234',
                'code': code
            }), follow_redirects=True)
        assert res.status_code == HTTPStatus.CREATED

    def test_login(self):
        self.test_signup()
        res = self.app.post(
            path='/user/login',
            content_type='application/json',
            data=json.dumps({
                'email': 'test@naver.com',
                'password': 'aA12341234!'
            }), follow_redirects=True)
        assert res.status_code == HTTPStatus.OK
        return res.json['response']['token']

    def test_update_password(self):
        self.test_signup()
        code = self.test_update_auth_phone()
        res = self.app.patch(
            path='/user/password',
            content_type='application/json',
            data=json.dumps({
                "email": "test@naver.com",
                "password": "bB12341234!",
                "phone": "01012341234",
                "code": code
            }), follow_redirects=True)

        assert res.status_code == HTTPStatus.OK
