from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.schemas.user_schema import CreateUserSchema, LoginUserSchema
from app.services import auth_service

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        schema = CreateUserSchema()
        validated_data = schema.load(data)
        user = auth_service.register(validated_data)

        return jsonify({'message': 'User created successfully',
                        'user': {
                            'id': user.id,
                            'name': user.name,
                            'email': user.email,
                            'phone_number': user.phoneNumber
                        }
                        }), 201

    except ValidationError as err:
        return jsonify({'message': err.messages}, 400)
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        schema = LoginUserSchema()
        validated_data = schema.load(data)
        result = auth_service.login(validated_data)

        if not result:
            return jsonify({'message': 'Login failed'}), 401
        return jsonify({'message': 'User logged in', 'token': result}), 200

    except ValidationError as err:
        return jsonify({'message': err.messages}, 400)
    except Exception as e:
        return jsonify({'message': str(e)}), 400