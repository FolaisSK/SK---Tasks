from datetime import datetime
from email.policy import default

from app.models.category import Category
from main import db


class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.Enum(Category), nullable=False)
    description = db.Column(db.Text, nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)