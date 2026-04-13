from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

from app.schemas.expense_schema import CreateExpenseSchema, FilterByDateRangeSchema
from app.services import expense_tracker_service

expense_bp = Blueprint('expenses', __name__)

@expense_bp.route('/add', methods=['POST'])
@jwt_required()
def add_expense():
    try:
        data = request.get_json()
        schema = CreateExpenseSchema()
        user_id = get_jwt_identity()
        data.update({'user_id': user_id})
        validated_data = schema.load(data)

        new_expense = expense_tracker_service.add_expense(validated_data)

        return jsonify({'message': "Expense created successfully!",
                        'data' : {
                            'id': new_expense.id,
                            'amount': new_expense.amount,
                            'category': new_expense.category.value,
                            'description': new_expense.description,
                        }
                        }), 201

    except ValidationError as err:
        return jsonify({'message': err.messages}, 400)
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@expense_bp.route('/view_all', methods=['GET'])
@jwt_required()
def view_all_expenses():
    try:
        user_id = get_jwt_identity()
        expenses = expense_tracker_service.view_all_expenses(user_id)
        return jsonify({'expenses': [
            {
                'id': exp.id,
                'amount': exp.amount,
                'category': exp.category.value,
                'description': exp.description,
                'transaction_date': str(exp.transaction_date)
            }
            for exp in expenses
        ]
                        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@expense_bp.route('/filter/category/<string:category>', methods=['GET'])
@jwt_required()
def view_expenses_by_category(category):
    try:
        user_id = get_jwt_identity()
        expenses = expense_tracker_service.filter_by_category(user_id, category)

        return jsonify({
            'expenses': [
                {
                    'id': exp.id,
                    'amount': exp.amount,
                    'category': exp.category.value,
                    'description': exp.description,
                    'transaction_date': str(exp.transaction_date)
                }
                for exp in expenses
            ]
        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@expense_bp.route('filter/date-range', methods=['GET'])
@jwt_required()
def view_expenses_by_date_range():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        schema = FilterByDateRangeSchema()
        data.update({'user_id': user_id})
        validated_data = schema.load(data)
        expenses = expense_tracker_service.filter_by_date_range(validated_data)

        return jsonify({
            'expenses': [
                {
                    'id': exp.id,
                    'amount': exp.amount,
                    'category': exp.category.value,
                    'description': exp.description,
                    'transaction_date': str(exp.transaction_date)
                }
                for exp in expenses
            ]
        })
    except Exception as e:
        return jsonify({'message': str(e)}), 400