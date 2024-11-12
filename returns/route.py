from flask import Blueprint, make_response, jsonify, request
from returns.service import ReturnService
from returns.repository import ReturnRepository

returns_bp = Blueprint("returns", __name__)
return_service = ReturnService(ReturnRepository())


@returns_bp.route("/returns", methods=["GET"])
def get_all_returns():
    returns = return_service.get_all_returns()
    return make_response(jsonify(data=[return_.to_dict() for return_ in returns]))


@returns_bp.route("/returns/<int:return_id>", methods=["GET"])
def get_return(return_id):
    return_record = return_service.get_return_by_id(return_id)
    if return_record:
        return make_response(jsonify(return_record.to_dict()))
    return make_response(jsonify({"error": "Return not found"}), 404)


@returns_bp.route("/returns", methods=["POST"])
def add_return():
    data = request.get_json()
    lending_id = data.get("lending_id")
    return_date = data.get("return_date")  # Debe estar en formato ISO (YYYY-MM-DD)
    condition = data.get("condition")
    new_return = return_service.add_return(lending_id, return_date, condition)
    return make_response(jsonify(new_return.to_dict()), 201)


@returns_bp.route("/returns/<int:return_id>", methods=["PUT"])
def update_return(return_id):
    data = request.get_json()
    lending_id = data.get("lending_id")
    return_date = data.get("return_date")  # Debe estar en formato ISO
    condition = data.get("condition")
    updated_return = return_service.update_return(
        return_id, lending_id, return_date, condition
    )
    if updated_return:
        return make_response(jsonify(updated_return.to_dict()))
    return make_response(jsonify({"error": "Return not found"}), 404)


@returns_bp.route("/returns/<int:return_id>", methods=["DELETE"])
def delete_return(return_id):
    deleted_return = return_service.delete_return(return_id)
    if deleted_return:
        return make_response(jsonify({"message": "Return deleted"}))
    return make_response(jsonify({"error": "Return not found"}), 404)
