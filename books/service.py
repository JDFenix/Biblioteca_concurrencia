from books.repository import BookRepository
from books.model import Book


class BookService:

    def __init__(self, book_repository: BookRepository) -> None:
        self.book_repository = book_repository

    def get_all_books(self):
        return self.book_repository.get_all_books()
