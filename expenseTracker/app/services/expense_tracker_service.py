from app.models.category import Category
from app.models.expense import Expense
from app.repositories import expense_repository
from app.schemas.expense_schema import CreateExpenseSchema, UpdateExpenseSchema, FilterByCategorySchema, \
    FilterByDateRangeSchema
from app.extensions import db


def add_expense(request : CreateExpenseSchema):
    if request['amount'] <= 0:
        raise Exception("Invalid amount")
    if request['category'] is None:
        raise Exception("Invalid category")

    expense = Expense(
        amount = request['amount'],
        category = Category(request['category']),
        description = request['description'],
        transaction_date = request['transaction_date'],
        user_id = request['user_id']
    )

    return expense_repository.save(expense)

def update_expense(request : UpdateExpenseSchema):
    if request['amount'] <= 0:
        raise Exception("Invalid amount")
    if request['category'] is None:
        raise Exception("Invalid category")

    # expense = Expense.query.get_or_404(request['expense_id'])
    expense = expense_repository.get_expenses_by_id(expense_id=request['expense_id'], user_id=request['user_id'])

    expense.amount = request['amount']
    expense.category = request['category']
    expense.description = request['description']
    expense.transaction_date = request['transaction_date']

    db.session.commit()
    return expense

def view_all_expenses(user_id):
    return expense_repository.get_all_expenses_by_user(user_id)

def delete_expense(expense_id, user_id):
    # expense = Expense.query.get_or_404(expense_id)
    expense = expense_repository.get_expenses_by_id(expense_id=expense_id, user_id=user_id)
    expense_repository.delete(expense)
    return "Expense deleted successfully!!!"

def filter_by_category(user_id, category):
    return expense_repository.get_expenses_by_category(category=category, user_id=user_id)

def filter_by_date_range(request : FilterByDateRangeSchema):
    return expense_repository.get_expenses_by_date_range(user_id=request['user_id'], start_date=request['start_date'],end_date=['end_date'])

