from app.models.user import User
from app.extensions import db


def save(user):
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_id(user_id):
    return User.query.filter_by(user_id=user_id).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def delete(user):
    user = User.query.filter_by(user_id=user.id).first()
    db.session.delete(user)
    db.session.commit()