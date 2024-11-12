from flask import Blueprint, make_response, jsonify, request
from lendings.service import LendingService
from lendings.repository import LendingRepository

lendings_bp = Blueprint("lendings", __name__)
lending_service = LendingService(LendingRepository())


@lendings_bp.route("/lendings", methods=["GET"])
def get_all_lendings():
    lendings = lending_service.get_all_lendings()
    return make_response(jsonify(data=[lending.to_dict() for lending in lendings]))


@lendings_bp.route("/lendings/<int:lending_id>", methods=["GET"])
def get_lending(lending_id):
    lending = lending_service.get_lending_by_id(lending_id)
    if lending:
        return make_response(jsonify(lending.to_dict()))
    return make_response(jsonify({"error": "Lending not found"}), 404)


@lendings_bp.route("/lendings", methods=["POST"])
def add_lending():
    data = request.get_json()
    user_id = data.get("user_id")
    book_id = data.get("book_id")
    return_id = data.get("return_id")
    new_lending = lending_service.add_lending(user_id, book_id, return_id)
    return make_response(jsonify(new_lending.to_dict()), 201)


@lendings_bp.route("/lendings/<int:lending_id>", methods=["PUT"])
def update_lending(lending_id):
    data = request.get_json()
    user_id = data.get("user_id")
    book_id = data.get("book_id")
    return_id = data.get("return_id")
    updated_lending = lending_service.update_lending(
        lending_id, user_id, book_id, return_id
    )
    if updated_lending:
        return make_response(jsonify(updated_lending.to_dict()))
    return make_response(jsonify({"error": "Lending not found"}), 404)


@lendings_bp.route("/lendings/<int:lending_id>", methods=["DELETE"])
def delete_lending(lending_id):
    deleted_lending = lending_service.delete_lending(lending_id)
    if deleted_lending:
        return make_response(jsonify({"message": "Lending deleted"}))
    return make_response(jsonify({"error": "Lending not found"}), 404)
