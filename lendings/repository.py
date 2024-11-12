from lendings.model import Lending
from db import db


class LendingRepository:

    @staticmethod
    def get_all_lendings():
        return Lending.query.all()

    @staticmethod
    def get_lending_by_id(lending_id):
        return Lending.query.get(lending_id)

    @staticmethod
    def add_lending(user_id, book_id, return_id=None):
        new_lending = Lending(user_id=user_id, book_id=book_id, return_id=return_id)
        db.session.add(new_lending)
        db.session.commit()
        return new_lending

    @staticmethod
    def update_lending(lending_id, user_id=None, book_id=None, return_id=None):
        lending = Lending.query.get(lending_id)
        if lending:
            if user_id:
                lending.user_id = user_id
            if book_id:
                lending.book_id = book_id
            if return_id:
                lending.return_id = return_id
            db.session.commit()
        return lending

    @staticmethod
    def delete_lending(lending_id):
        lending = Lending.query.get(lending_id)
        if lending:
            db.session.delete(lending)
            db.session.commit()
        return lending
