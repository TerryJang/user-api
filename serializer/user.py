from marshmallow import Schema, fields


class UserBaseSchema(Schema):
    email = fields.String(required=True)
    name = fields.String(required=True)
    nickname = fields.String(required=True)
    phone = fields.String(required=True)


class UserInfoResponseSchema(UserBaseSchema):
    created = fields.String()


class UserSignUpRequestSchema(UserBaseSchema):
    password = fields.String(required=True)


class UserLoginRequestSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)
