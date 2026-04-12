from marshmallow import Schema, fields


class CreateExpenseSchema(Schema):
    amount = fields.Float(required=True)
    category = fields.String(required=True)
    description = fields.String(required=True)
    transaction_date = fields.DateTime(required=True)
    user_id = fields.Integer(required=True)

class UpdateExpenseSchema(Schema):
    expense_id = fields.Integer(required=True)
    amount = fields.Float(required=True)
    category = fields.String(required=True)
    description = fields.String(required=True)
    transaction_date = fields.DateTime(required=True)