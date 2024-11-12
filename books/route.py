from flask import Blueprint, make_response, jsonify, request
from books.service import BookService
from books.repository import BookRepository


books_bp = Blueprint("/books", __name__)
book_service = BookService(BookRepository())


@books_bp.route("/books", methods=["GET"])
def get_all_books():
    books = book_service.get_all_books()
    return make_response(jsonify(data=[book.to_dict() for book in books]))
