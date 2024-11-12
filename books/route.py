# books/routes.py
from flask import Blueprint, make_response, jsonify, request
from books.service import BookService
from books.repository import BookRepository

books_bp = Blueprint("books", __name__)
book_service = BookService(BookRepository())


@books_bp.route("/books", methods=["GET"])
def get_all_books():
    books = book_service.get_all_books()
    return make_response(jsonify(data=[book.to_dict() for book in books]))


@books_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = book_service.get_book_by_id(book_id)
    if book:
        return make_response(jsonify(book.to_dict()))
    return make_response(jsonify({"error": "Book not found"}), 404)


@books_bp.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    image = data.get("image")
    author_id = data.get("author_id")
    new_book = book_service.add_book(name, description, image, author_id)
    return make_response(jsonify(new_book.to_dict()), 201)


@books_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    image = data.get("image")
    updated_book = book_service.update_book(book_id, name, description, image)
    if updated_book:
        return make_response(jsonify(updated_book.to_dict()))
    return make_response(jsonify({"error": "Book not found"}), 404)


@books_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    deleted_book = book_service.delete_book(book_id)
    if deleted_book:
        return make_response(jsonify({"message": "Book deleted"}))
    return make_response(jsonify({"error": "Book not found"}), 404)
