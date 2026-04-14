from marshmallow import Schema, fields


class CreateExpenseSchema(Schema):
    amount = fields.Float(required=True)
    category = fields.String(required=True)
    description = fields.String(required=True)
    transaction_date = fields.Date(required=False)
    user_id = fields.Integer(required=True)

class UpdateExpenseSchema(Schema):
    expense_id = fields.Integer(required=True)
    amount = fields.Float(required=True)
    category = fields.String(required=True)
    description = fields.String(required=True)
    transaction_date = fields.Date(required=True)
    user_id = fields.Integer(required=True)

class FilterByCategorySchema(Schema):
    category = fields.String(required=True)
    user_id = fields.Integer(required=True)

class FilterByDateRangeSchema(Schema):
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    user_id = fields.Integer(required=True)