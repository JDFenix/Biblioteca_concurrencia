from books.repository import BookRepository


class BookService:

    def __init__(self, book_repository: BookRepository) -> None:
        self.book_repository = book_repository

    def get_all_books(self):
        return self.book_repository.get_all_books()

    def get_book_by_id(self, book_id):
        return self.book_repository.get_book_by_id(book_id)

    def add_book(self, name, description, image, author_id):
        return self.book_repository.add_book(name, description, image, author_id)

    def update_book(self, book_id, name=None, description=None, image=None):
        return self.book_repository.update_book(book_id, name, description, image)

    def delete_book(self, book_id):
        return self.book_repository.delete_book(book_id)
