from flask import Blueprint, make_response, jsonify, request
from authors.service import AuthorService
from authors.repository import AuthorRepository

authors_bp = Blueprint("authors", __name__)
author_service = AuthorService(AuthorRepository())


@authors_bp.route("/authors", methods=["GET"])
def get_all_authors():
    authors = author_service.get_all_authors()
    return make_response(jsonify(data=[author.to_dict() for author in authors]))


@authors_bp.route("/authors/<int:author_id>", methods=["GET"])
def get_author(author_id):
    author = author_service.get_author_by_id(author_id)
    if author:
        return make_response(jsonify(author.to_dict()))
    return make_response(jsonify({"error": "Author not found"}), 404)


@authors_bp.route("/authors", methods=["POST"])
def add_author():
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    birth_year = data.get("birth_year")
    new_author = author_service.add_author(first_name, last_name, birth_year)
    return make_response(jsonify(new_author.to_dict()), 201)


@authors_bp.route("/authors/<int:author_id>", methods=["PUT"])
def update_author(author_id):
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    birth_year = data.get("birth_year")
    updated_author = author_service.update_author(
        author_id, first_name, last_name, birth_year
    )
    if updated_author:
        return make_response(jsonify(updated_author.to_dict()))
    return make_response(jsonify({"error": "Author not found"}), 404)


authors_bp.route("/authors/<int:author_id>", methods=["DELETE"])


def delete_author(author_id):
    deleted_author = author_service.delete_author(author_id)
    if deleted_author:
        return make_response(jsonify({"message": "Author deleted"}))
    return make_response(jsonify({"error": "Author not found"}), 404)
