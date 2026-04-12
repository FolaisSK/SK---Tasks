from marshmallow import Schema, fields, validate


class CreateUserSchema(Schema):
    name: fields.String(required=True, validate=validate.Length(min=3, max=50))
    email: fields.Email(required=True)
    phone: fields.String(required=True, validate=validate.Length(min=11, max=11))
    password: fields.String(required=True, validate=validate.Length(min=8, max=26))

class LoginUserSchema(Schema):
    email: fields.Email(required=True)
    password: fields.String(required=True, validate=validate.Length(min=8, max=26))

class LoginResponseSchema(Schema):
    email: fields.Email(required=True)
    user_id: fields.Integer(required=True)
    token: fields.String(required=True)