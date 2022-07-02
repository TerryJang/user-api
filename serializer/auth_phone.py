from marshmallow import Schema, fields


class AuthPhoneCreateRequestSchema(Schema):
    phone = fields.String()


class AuthPhoneUpdateRequestSchema(Schema):
    phone = fields.String()
    code = fields.String()
