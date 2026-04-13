from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.user import User
from app.repositories import user_repository
from app.schemas.user_schema import CreateUserSchema, LoginUserSchema, LoginResponseSchema


def register(request : CreateUserSchema):
    hashed_password = generate_password_hash(request['password'])

    user = user_repository.get_user_by_email(email=request['email'])
    if user:
        raise Exception('User already exists')

    new_user = User(
        name=request['name'],
        email=request['email'],
        phoneNumber=request['phoneNumber'],
        password=hashed_password
    )

    return user_repository.save(new_user)

def login(request : LoginUserSchema):
    user = user_repository.get_user_by_email(email=request['email'])
    if not user:
        return False
    if not check_password_hash(pwhash=user.password, password=request['password']):
        return None
    token = create_access_token(identity=str(user.id))

    return token