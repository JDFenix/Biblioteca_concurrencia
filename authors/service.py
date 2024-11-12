from authors.repository import AuthorRepository


class AuthorService:

    def __init__(self, author_repository: AuthorRepository) -> None:
        self.author_repository = author_repository

    def get_all_authors(self):
        return self.author_repository.get_all_authors()

    def get_author_by_id(self, author_id):
        return self.author_repository.get_author_by_id(author_id)

    def add_author(self, first_name, last_name, birth_year):
        return self.author_repository.add_author(first_name, last_name, birth_year)

    def update_author(
        self, author_id, first_name=None, last_name=None, birth_year=None
    ):
        return self.author_repository.update_author(
            author_id, first_name, last_name, birth_year
        )

    def delete_author(self, author_id):
        return self.author_repository.delete_author(author_id)
