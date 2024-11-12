from books.model import Book
from db import db


class BookRepository:

    @staticmethod
    def add_book(name, description, image):
        new_book = Book(name=name, description=description, image=image)
        db.session.add(new_book)
        db.session.commit()
        return new_book

    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def get_all_books():
        return Book.query.all()

    @staticmethod
    def update_book(book_id, name=None, description=None, image=None):
        book = Book.query.get(book_id)
        if book:
            if name:
                book.name = name
            if description:
                book.description = description
            if image:
                book.image = image
            db.session.commit()
        return book

    @staticmethod
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
        return book
