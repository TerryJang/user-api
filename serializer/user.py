from marshmallow import Schema, fields, validates_schema, ValidationError

from common.utils import Utils


class UserBaseSchema(Schema):
    email = fields.String(required=True)
    name = fields.String(required=True)
    nickname = fields.String(required=True)
    phone = fields.String(required=True)


class UserInfoResponseSchema(UserBaseSchema):
    created_at = fields.String()


class UserSignUpRequestSchema(UserBaseSchema):
    password = fields.String(required=True)
    code = fields.String(required=True)

    @validates_schema
    def validate_signup_data(self, data, **kwargs):
        for key in data:
            if key == 'email':
                result = Utils.validate_email(data[key])
                if result is False:
                    raise ValidationError('유효하지 않은 이메일 입니다.')

            if key == 'password':
                pass

            if key == 'phone':
                pass


class UserLoginRequestSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)


class UserUpdatePasswordRequestSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)
    phone = fields.String(required=True)
    code = fields.String(required=True)
