from app.models.expense import Expense
from app.extensions import db


def save(expense):
    db.session.add(expense)
    db.session.commit()
    return expense

def get_all_expenses_by_user(user_id):
    return Expense.query.filter_by(user_id=user_id).all()

def get_expenses_by_id(expense_id,user_id):
    return Expense.query.filter_by(expense_id=expense_id,user_id=user_id).first()

def get_expenses_by_category(user_id, category):
    return Expense.query.filter_by(user_id=user_id, category=category).all()

def get_expenses_by_date_range(user_id, start_date, end_date):
    return (Expense.query.filter(Expense.user_id==user_id,
                                Expense.transaction_date>=start_date,
                                Expense.transaction_date<=end_date).all())

def delete(expense):
    db.session.delete(expense)
    db.session.commit()