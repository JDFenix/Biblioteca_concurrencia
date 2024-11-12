# authors/repository.py
from authors.model import Author
from db import db


class AuthorRepository:

    @staticmethod
    def add_author(first_name, last_name, birth_year):
        new_author = Author(
            first_name=first_name, last_name=last_name, birth_year=birth_year
        )
        db.session.add(new_author)
        db.session.commit()
        return new_author

    @staticmethod
    def get_author_by_id(author_id):
        return Author.query.get(author_id)

    @staticmethod
    def get_all_authors():
        return Author.query.all()

    @staticmethod
    def update_author(author_id, first_name=None, last_name=None, birth_year=None):
        author = Author.query.get(author_id)
        if author:
            if first_name:
                author.first_name = first_name
            if last_name:
                author.last_name = last_name
            if birth_year:
                author.birth_year = birth_year
            db.session.commit()
        return author

    @staticmethod
    def delete_author(author_id):
        author = Author.query.get(author_id)
        if author:
            db.session.delete(author)
            db.session.commit()
        return author
