from flask import Blueprint, make_response, jsonify, request
from users.service import UserService
from users.repository import UserRepository

users_bp = Blueprint("users", __name__)
user_service = UserService(UserRepository())


@users_bp.route("/users", methods=["GET"])
def get_all_users():
    users = user_service.get_all_users()
    return make_response(jsonify(data=[user.to_dict() for user in users]), 200)


@users_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return make_response(jsonify(data=user.to_dict()), 200)
    else:
        return make_response(jsonify(message="User not found"), 404)


@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data["username"], data["email"])
    return make_response(jsonify(data=user.to_dict()), 201)


@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = user_service.update_user(user_id, data.get("username"), data.get("email"))
    if user:
        return make_response(jsonify(data=user.to_dict()), 200)
    else:
        return make_response(jsonify(message="User not found"), 404)


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = user_service.delete_user(user_id)
    if user:
        return make_response(jsonify(message="User deleted"), 200)
    else:
        return make_response(jsonify(message="User not found"), 404)
