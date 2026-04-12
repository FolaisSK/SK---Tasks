from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.routers.auth_router import auth_bp
from app.routers.expense_tracker_router import expense_bp

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

jwt = JWTManager(app)
db = SQLAlchemy(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(expense_bp, url_prefix="/expenses")

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=8000)