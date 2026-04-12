from app.models.expense import Expense
from app.schemas.expense_schema import CreateExpenseSchema, UpdateExpenseSchema
from main import db


def add_expense(request : CreateExpenseSchema):
    expense = Expense(
        amount = request.amount,
        category = request.category,
        description = request.description,
        transaction_date = request.transaction_date,
        user_id = request.user_id,
    )
    db.session.add(expense)
    db.session.commit()
    return expense

def update_expense(request : UpdateExpenseSchema):
    expense = Expense.query.get_or_404(request.expense_id)
    expense.amount = request.amount
    expense.category = request.category
    expense.description = request.description
    expense.transaction_date = request.transaction_date

    db.session.add(expense)
    db.session.commit()
    return expense

def view_all_expenses(user_id):
    expenses = Expense.query.filter_by(user_id = user_id).all()
    return expenses

def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return "Expense deleted successfully!!!"