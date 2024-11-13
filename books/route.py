# books/routes.py
from flask import Blueprint, make_response, jsonify, request, render_template
from sqlalchemy.orm import joinedload
from books.service import BookService
from books.repository import BookRepository
from authors.model import Author
from books.model import Book

books_bp = Blueprint("books", __name__)
books_views_bp = Blueprint("books_views", __name__, template_folder="templates")

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


@books_views_bp.route("/home")
def home():
    all_books = Book.query.options(joinedload(Book.author)).limit(8).all()
    books_with_authors = []
    for book in all_books:
        author = Author.query.get(book.author_id)
        books_with_authors.append({"book": book, "author": author})
        print(book.name)
    return render_template("home.html", books=books_with_authors)
